import TaskItem from './TaskItem';

function TaskList({ title, tasks, onToggleComplete, onDelete, emptyMessage, color }) {
  // RENDERIZADO CONDICIONAL
  if (tasks.length === 0) {
    return (
      <div className="task-column">
        <div className="column-header" style={{ borderColor: color }}>
          <h3>{title}</h3>
          <span className="task-count">0</span>
        </div>
        <div className="column-content">
          <div className="empty-column">
            <p>{emptyMessage}</p>
          </div>
        </div>
      </div>
    );
  }
  
  // RENDERIZADO DE LISTAS con map()
  return (
    <div className="task-column">
      <div className="column-header" style={{ borderColor: color }}>
        <h3>{title}</h3>
        <span className="task-count">{tasks.length}</span>
      </div>
      <div className="column-content">
        {tasks.map(task => (
          <TaskItem
            key={task.id}
            task={task}
            onToggleComplete={onToggleComplete}
            onDelete={onDelete}
          />
        ))}
      </div>
    </div>
  );
}

export default TaskList;