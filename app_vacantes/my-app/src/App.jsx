import { useState, useEffect } from 'react';
import Header from './components/Header';
import TaskForm from './components/TaskForm';
import TaskList from './components/TaskList';
import './App.css';

function App() {
  // ========== ESTADO CON useState ==========
  const [tasks, setTasks] = useState(() => {
    const savedTasks = localStorage.getItem('tasks');
    return savedTasks ? JSON.parse(savedTasks) : [];
  });

  const [showTaskForm, setShowTaskForm] = useState(false);

  // ========== EFECTO PARA PERSISTENCIA ==========
  useEffect(() => {
    localStorage.setItem('tasks', JSON.stringify(tasks));
  }, [tasks]);

  // ========== FUNCIONES REQUERIDAS ==========
  
  // 1. Agregar tarea
  const handleAddTask = (text) => {
    const newTask = {
      id: Date.now(),
      text: text.trim(),
      completed: false,
      createdAt: new Date().toISOString(),
      completedAt: null
    };
    
    // SIN MUTACIÓN DIRECTA
    setTasks(prevTasks => [newTask, ...prevTasks]);
    setShowTaskForm(false);
    alert('✅ ¡Tarea agregada correctamente!');
  };

  // 2. Marcar como completada
  const handleToggleComplete = (id) => {
    // SIN MUTACIÓN DIRECTA
    setTasks(prevTasks => 
      prevTasks.map(task => {
        if (task.id === id) {
          return {
            ...task,
            completed: !task.completed,
            completedAt: !task.completed ? new Date().toISOString() : null
          };
        }
        return task;
      })
    );
  };

  // 3. Eliminar tarea
  const handleDeleteTask = (id) => {
    if (window.confirm('¿Estás seguro de eliminar esta tarea?')) {
      // SIN MUTACIÓN DIRECTA
      setTasks(prevTasks => prevTasks.filter(task => task.id !== id));
    }
  };

  // ========== DATOS DERIVADOS ==========
  const pendingTasks = tasks.filter(task => !task.completed);
  const completedTasks = tasks.filter(task => task.completed);

  return (
    <div className="app-container">
      {/* ===== HEADER CON ESTADÍSTICAS ===== */}
      <Header 
        totalTasks={tasks.length}
        pendingTasks={pendingTasks.length}
        completedTasks={completedTasks.length}
        onAddTask={() => setShowTaskForm(true)}
      />
      
      {/* ===== CONTENIDO PRINCIPAL ===== */}
      <main className="main-content">
        {/* ===== COLUMNAS DE TAREAS ===== */}
        <div className="tasks-columns">
          {/* COLUMNA: TAREAS PENDIENTES */}
          <TaskList
            title="📥 Pendientes"
            tasks={pendingTasks}
            onToggleComplete={handleToggleComplete}
            onDelete={handleDeleteTask}
            emptyMessage="🎉 ¡No hay tareas pendientes!"
            color="#FF6B6B"
          />
          
          {/* COLUMNA: TAREAS COMPLETADAS */}
          <TaskList
            title="✅ Completadas"
            tasks={completedTasks}
            onToggleComplete={handleToggleComplete}
            onDelete={handleDeleteTask}
            emptyMessage="📭 Aún no has completado tareas"
            color="#51CF66"
          />
        </div>
      </main>

      {/* ===== MODAL PARA AGREGAR TAREAS ===== */}
      {showTaskForm && (
        <div className="modal-overlay" onClick={() => setShowTaskForm(false)}>
          <div className="modal-content" onClick={(e) => e.stopPropagation()}>
            <TaskForm 
              onAddTask={handleAddTask}
              onClose={() => setShowTaskForm(false)}
            />
          </div>
        </div>
      )}
    </div>
  );
}

export default App;