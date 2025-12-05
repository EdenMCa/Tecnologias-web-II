import { useState, useEffect } from 'react'; // Importamos hooks de React para manejar estado y efectos.
import Header from './components/Header';
import TaskForm from './components/TaskForm'; // Importamos el formulario para agregar tareas (modal).
import TaskList from './components/TaskList';
import './App.css';

function App() {
  // ========== ESTADO CON useState ==========
  const [tasks, setTasks] = useState(() => {
    const savedTasks = localStorage.getItem('tasks');// Obtenemos las tareas guardadas del localStorage
    return savedTasks ? JSON.parse(savedTasks) : [];     // Si existen tareas guardadas, las convierte de texto a array; si no, inicia con un array vacío
  });

  const [showTaskForm, setShowTaskForm] = useState(false); // Estado para controlar la visibilidad del formulario de tareas

  // ========== EFECTO PARA PARA GUARDAR CAMBIOS EN LOCALSTORAGE ==========
  useEffect(() => {
    localStorage.setItem('tasks', JSON.stringify(tasks));     // Cada vez que "tasks" cambia, lo guardamos en localStorage
  }, [tasks]);

  // ========== FUNCIONES PRINCIPALES ==========
  
  // 1. Agregar tarea
  
  const handleAddTask = (text) => { 
    const nuevaTarea = { // Creamos un nuevo objeto tarea
      id: Date.now(), // ID único basado en timestamp
      text: text.trim(), // Texto de la tarea, eliminando espacios en blanco al inicio y final
      completed: false, // Al crear una tarea el sistema la marca como pendiente
      createdAt: new Date().toISOString(), // Fecha de creación en formato ISO
      completedAt: null   // Fecha de completación, inicialmente nula
    };
    
    // Actualizamos el estado SIN modificar el arreglo original
    setTasks(prevTasks => [nuevaTarea, ...prevTasks]);
    setShowTaskForm(false); // Cerramos el formulario de tareas al agregar una nueva tarea  
    alert('✅ ¡Tarea agregada correctamente!'); // Mostramos una alerta de éxito
  };

  // 2. Marcar o desmarca una tarea como completada
  const handleToggleComplete = (id) => {
    setTasks(prevTasks =>     // Transformamos el array sin mutarlo  
      prevTasks.map(task => { // Recorremos cada tarea 
        if (task.id === id) { // Si encontramos la tarea con el ID correspondiente
          return { // Retornamos una nueva tarea con el estado "completed" invertido
            ...task, // Copiamos las propiedades existentes de la tarea
            completed: !task.completed, // Invertimos el estado de completado
            completedAt: !task.completed ? new Date().toISOString() : null // Actualizamos la fecha de completación
          };
        }
        return task; // Si no es la tarea buscada, la retornamos sin cambios
      })
    );
  };

  // 3. Eliminar tarea
  const handleDeleteTask = (id) => {
    if (window.confirm('¿Estás seguro de eliminar esta tarea?')) {
      setTasks(prevTasks => prevTasks.filter(task => task.id !== id)); // Filtramos la tarea a eliminar
      alert('🗑️ Tarea eliminada correctamente'); // Mostramos una alerta de éxito
    }
  };

  const pendingTasks = tasks.filter(task => !task.completed); // Filtramos las tareas pendientes
  const completedTasks = tasks.filter(task => task.completed); // Filtramos las tareas completadas

  return (
    <div className="app-container">
      {/* ===== HEADER CON ESTADÍSTICAS ===== */}
      <Header 
        totalTasks={tasks.length} // Pasamos el total de tareas
        pendingTasks={pendingTasks.length} // Pasamos el total de tareas pendientes
        completedTasks={completedTasks.length} // Pasamos el total de tareas completadas
        onAddTask={() => setShowTaskForm(true)} // Función para mostrar el formulario de tareas
      />
      
      {/* ===== CONTENIDO PRINCIPAL ===== */}
      <main className="main-content">
        {/* ===== COLUMNAS DE TAREAS ===== */}
        <div className="tasks-columns">

          {/* COLUMNA: TAREAS PENDIENTES */}
          <TaskList
            title="⚠️ Pendientes" // Titulo 
            tasks={pendingTasks} // Pasamos las tareas pendientes
            onToggleComplete={handleToggleComplete}  // Función para marcar como completada
            onDelete={handleDeleteTask}  // Función para eliminar tarea
            emptyMessage="🎉 ¡No hay tareas pendientes!" // Mostramos este mensaje cuando no haya tareas pendientes
            color="#FF6B6B" // Color rojo para la columna de tareas pendientes
          />
          
          {/* COLUMNA: TAREAS COMPLETADAS */}
          <TaskList
            title="✅ Completadas"
            tasks={completedTasks} // Pasamos las tareas completadas
            onToggleComplete={handleToggleComplete} // Función para desmarcar como completada
            onDelete={handleDeleteTask} // Función para eliminar tarea
            emptyMessage="📭 Aún no has completado tareas"  
            color="#51CF66" // Color verde para la columna de tareas completadas
          />
        </div>
      </main>

      {/* ===== MODAL PARA AGREGAR TAREAS ===== */}
      {showTaskForm && ( // Si showTaskForm es true, mostramos el modal
        // Evita que el modal se cierre al hacer clic dentro de él
        <div className="modal-overlay" onClick={() => setShowTaskForm(false)}> 
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <TaskForm 
              onAddTask={handleAddTask} // Función para agregar tarea
              onClose={() => setShowTaskForm(false)} // Función para cerrar el modal
            />
          </div>
        </div>
      )}
    </div>
  );
}

export default App; // Exportamos el componente para usarlo en toda la app