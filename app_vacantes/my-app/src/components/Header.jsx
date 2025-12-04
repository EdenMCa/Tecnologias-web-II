function Header({ totalTasks, pendingTasks, completedTasks, onAddTask }) { // Componente Header que recibe props desde App.jsx
  const completionRate = totalTasks > 0 ? Math.round((completedTasks / totalTasks) * 100) : 0;   // Calcula el porcentaje de tareas completadas.   
  // Si totalTasks es mayor a 0, calcula el porcentaje; si no, devuelve 0.
  
  return (
    <header className="main-header">
      <div className="header-top"> {/* Zona superior del header, contiene el logo/título y el botón */}
        <div className="logo-section">
            <h1>Gestor de Tareas Personales</h1>
            <p className="tagline">Personal Space - Mendoza Casarrubia Rosendo Eden</p>
        </div>
        
        <button className="add-task-button" onClick={onAddTask}> {/* Botón para agregar nueva tarea */}
          <span className="button-icon">+</span> Nueva Tarea
        </button>
      </div>
      
      {/* ===== ESTADÍSTICAS EN EL HEADER ===== */}
      <div className="header-stats"> 
        <div className="stats-container"> {/* Contenedor de los valores numéricos de estadísticas */}
          <div className="stat-item">  {/* Elemento: total de tareas */}
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
        
        <div className="progress-container"> {/* Barra de progreso visual */}
          <div className="progress-bar">
           {/* Parte rellena de la barra, su ancho depende del completionRate */}
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