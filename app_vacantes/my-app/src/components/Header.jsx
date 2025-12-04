function Header({ totalTasks, pendingTasks, completedTasks, onAddTask }) {
  const completionRate = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;
  
  return (
    <header className="main-header">
      <div className="header-top">
        <div className="logo-section">
          <h1>Gestor de Tareas Personales</h1>
          <p className="tagline">Tecnologias Web II - Mendoza Casarrubia Rosendo Eden</p>
        </div>
        <button className="add-task-button" onClick={onAddTask}>
          <span className="button-icon">+</span>
          Nueva Tarea
        </button>
      </div>
      
      {/* ===== ESTADÍSTICAS EN EL HEADER ===== */}
      <div className="header-stats">
        <div className="stats-container">
          <div className="stat-item">
            <div className="stat-label">TOTAL</div>
            <div className="stat-number">{totalTasks}</div>
          </div>
          
          <div className="stat-item">
            <div className="stat-label">PENDIENTES</div>
            <div className="stat-number pending">{pendingTasks}</div>
          </div>
          
          <div className="stat-item">
            <div className="stat-label">COMPLETADAS</div>
            <div className="stat-number completed">{completedTasks}</div>
          </div>
          
          <div className="stat-item">
            <div className="stat-label">PROGRESO</div>
            <div className="stat-number progress">{completionRate}%</div>
          </div>
        </div>
        
        <div className="progress-container">
          <div className="progress-bar">
            <div 
              className="progress-fill" 
              style={{ width: `${completionRate}%` }}
            ></div>
          </div>
          <div className="progress-text">
            {completedTasks} de {totalTasks} tareas completadas
          </div>
        </div>
      </div>
    </header>
  );
}

export default Header;