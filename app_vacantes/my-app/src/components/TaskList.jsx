import TaskItem from './TaskItem';

function TaskList({ title, tasks, onToggleComplete, onDelete, emptyMessage, color }) { // Componente para listar tareas
  // RENDERIZADO CONDICIONAL
  if (tasks.length === 0) { // Si no hay tareas, mostramos un mensaje especial
    return (
      <div className="task-column">
        <div className="column-header" style={{ borderColor: color }}> {/* Encabezado de la columna con un borde cuyo color llega como prop */}
          <h3>{title}</h3>
          <span className="task-count">0</span> {/* Contador de tareas */}
        </div>
        <div className="column-content">
          <div className="empty-column">
            <p>{emptyMessage}</p> {/* Mensaje personalizado cuando no hay tareas */}
          </div>
        </div>
      </div>
    );
  }
  
  // ========== SI HAY TAREAS, SE MUESTRA LA LISTA ==========
  // RENDERIZADO DE LISTAS con map()
  return (
    <div className="task-column"> {/* Contenedor principal de la columna de tareas */}
      <div className="column-header" style={{ borderColor: color }}> {/* Encabezado de la columna con un borde cuyo color llega como prop */}
        <h3>{title}</h3>
        <span className="task-count">{tasks.length}</span> {/* Contador de tareas */}
      </div>
      <div className="column-content">
        {tasks.map(task => ( // Recorremos el array de tareas y renderizamos un TaskItem por cada una
          <TaskItem
            key={task.id} // Usamos el ID de la tarea como key única
            task={task} // Pasamos la tarea completa como prop
            onToggleComplete={onToggleComplete} // Pasamos la función para marcar como completada
            onDelete={onDelete} // Pasamos la función para eliminar tarea
          />
        ))}
      </div>
    </div>
  );
}

export default TaskList; // Exportamos el componente para usarlo en App.jsx