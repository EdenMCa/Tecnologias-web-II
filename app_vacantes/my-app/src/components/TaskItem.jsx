function TaskItem({ task, onToggleComplete, onDelete }) {
  // Función auxiliar para formatear fecha para mostrarla en la pantalla de la tarea
  const formatDate = (dateString) => { 
    if (!dateString) return ''; // Si no hay fecha, devuelve una cadena vacía
    const date = new Date(dateString); // Creamos un objeto Date a partir de la cadena
    return date.toLocaleDateString('es-ES', { // Formateamos la fecha en español, dia mes, hora y minuto
      day: '2-digit',
      month: 'short',
      hour: '2-digit',
      minute: '2-digit'
    });
  };
  
  return (
    // Clase condicional: si la tarea está completada, agrega la clase "completed"
    <div className={`task-item ${task.completed ? 'completed' : 'pending'}`}>
      <div className="task-content">

        {/* RENDERIZADO CONDICIONAL EN LÍNEA */}
        <p className={task.completed ? 'completed-text' : ''}> {/* Si la tarea está completada, se añade un emoji de palomita dentro del texto */}
          {task.text}
          {task.completed && ' ✅'}
        </p>
        <div className="task-dates">
          <small>Creada: {formatDate(task.createdAt)}</small> {/* Mostramos la fecha de creación siempre */}
          {/* Mostramos la fecha de completación solo si la tarea está marcada como completada */}
          {task.completed && (
            <small>Completada: {formatDate(task.completedAt)}</small> 
          )}
        </div>
      </div>
      
      <div className="task-actions">
        {/* Botón para MARCAR como completada */}
        <button
          className={`btn ${task.completed ? 'btn-secondary' : 'btn-primary'}`} // Clase condicional para el botón cambia según el estado de la tarea
          onClick={() => onToggleComplete(task.id)} // Llamamos a la función onToggleComplete pasando el ID de la tarea
        >
          {task.completed ? '↩️ Desmarcar' : '☑️ Completar'}
        </button>
        
        {/* Botón para ELIMINAR TAREA */}
        <button
          className="btn btn-danger"
          onClick={() => onDelete(task.id)} // Llamamos a la función onDelete pasando el ID de la tarea
        >
          🗑️ Eliminar
        </button>
      </div>
    </div>
  );
}

export default TaskItem;