import { useState } from 'react';

function TaskForm({ onAddTask, onClose }) {
  // ESTADO LOCAL con useState
  const [taskText, setTaskText] = useState('');
  
  // MANEJO DE EVENTOS
  const handleSubmit = (e) => {
    e.preventDefault();
        
    // 1. La tarea agregada no puede estar vacía, por lo tanto, nos debe arrojar una alerta
    if (!taskText.trim()) {
      alert('Error: La tarea no puede estar vacía');
      return;
    }
    
    // 2. La tarea debe tener al menos 3 palabras para ser válida
    const words = taskText.trim().split(/\s+/).filter(word => word.length > 0);
    if (words.length < 3) {
      alert(`Error: La tarea debe tener al menos 3 palabras\nPalabras actuales: ${words.length}`);
      return;
    }
    
    // 3. La tarea no puede exceder los 150 caracteres
    if (taskText.length > 150) {
      alert(`Error: La tarea no puede tener más de 150 caracteres\nCaracteres actuales: ${taskText.length}`);
      return;
    }
    
    // Si pasa todas las validaciones, se agrega la tarea
    onAddTask(taskText);
  };
  
  const handleChange = (e) => {
    setTaskText(e.target.value);
  };
  
  // Cálculos para mostrar al usuario sobre la longitud de la tarea
  const charCount = taskText.length;
  const wordCount = taskText.trim().split(/\s+/).filter(word => word.length > 0).length;
  const isValid = wordCount >= 3 && charCount <= 150 && taskText.trim() !== '';
  
  return (
    <div className="task-form-modal">
      <div className="modal-header">
        <h2>Nueva Tarea</h2>
        <button className="close-btn" onClick={onClose}>×</button>
      </div>
      
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Descripción de la tarea:</label>
          <textarea
            value={taskText}
            onChange={handleChange}
            placeholder="Ej: Examen del segundo parcial de Tecnologías Web II"
            rows="4"
            className="form-input"
            autoFocus
          />
          <div className="form-info">
            {/* USO DE LLAVES {} para expresiones JavaScript */}
            <span className={wordCount < 3 ? 'text-warning' : ''}>
              📝 Palabras: {wordCount}/3
            </span>
            <span className={charCount > 150 ? 'text-error' : ''}>
              🔤 Caracteres: {charCount}/150
            </span>
          </div>
        </div>
        
        <div className="form-actions">
          <button 
            type="button" 
            className="btn btn-secondary"
            onClick={onClose}
          >
            Cancelar
          </button>
          <button 
            type="submit" 
            className="btn btn-primary"
          >
            Agregar Tarea
          </button>
        </div>
      </form>
    </div>
  );
}

export default TaskForm;