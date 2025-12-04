function TaskItem({ task, onToggleComplete, onDelete }) {
  // Función auxiliar para formatear fecha para mostrarla en la pantalla de la tarea
  const formatDate = (dateString) => {
    if (!dateString) return '';
    const date = new Date(dateString);
    return date.toLocaleDateString('es-ES', {
      day: '2-digit',
      month: 'short',
      hour: '2-digit',
      minute: '2-digit'
    });
  };
  
  return (
    <div className={`task-item ${task.completed ? 'completed' : 'pending'}`}>
      <div className="task-content">
        {/* RENDERIZADO CONDICIONAL en línea */}
        <p className={task.completed ? 'completed-text' : ''}>
          {task.text}
          {task.completed && ' ✅'}
        </p>
        <div className="task-dates">
          <small>Creada: {formatDate(task.createdAt)}</small>
          {task.completed && (
            <small>Completada: {formatDate(task.completedAt)}</small>
          )}
        </div>
      </div>
      
      <div className="task-actions">
        {/* Botón para MARCAR COMO COMPLETADA */}
        <button
          className={`btn ${task.completed ? 'btn-secondary' : 'btn-primary'}`}
          onClick={() => onToggleComplete(task.id)}
        >
          {task.completed ? '↩️ Desmarcar' : '✓ Completar'}
        </button>
        
        {/* Botón para ELIMINAR TAREA */}
        <button
          className="btn btn-danger"
          onClick={() => onDelete(task.id)}
        >
          🗑️ Eliminar
        </button>
      </div>
    </div>
  );
}

export default TaskItem;