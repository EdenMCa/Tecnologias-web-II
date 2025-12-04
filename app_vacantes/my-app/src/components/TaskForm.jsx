import { useState } from 'react'; // Importamos useState para manejar estados locales dentro del componente

function TaskForm({ onAddTask, onClose }) { // Componente TaskForm, recibe las funciones onAddTask y onClose como props
  const [taskText, setTaskText] = useState(''); // Estado local para almacenar el texto de la tarea ingresada por el usuario
  
  // MANEJO DE EVENTOS
  const handleSubmit = (e) => { // Esta función se ejecuta cuando se envía el formulario
    e.preventDefault(); // Evita que la página se recargue al enviar el formulario
        
    // 1. La tarea agregada no puede estar vacía, por lo tanto, nos debe arrojar una alerta
    if (!taskText.trim()) {
      alert('Error: La tarea no puede estar vacía');
      return; // Salimos de la función si la tarea está vacía
    }
    
    // 2. La tarea debe tener al menos 3 palabras para ser válida
    const words = taskText.trim().split(/\s+/).filter(word => word.length > 0); // Dividimos el texto en palabras y filtramos las vacías
    if (words.length < 3) { // Si hay menos de 3 palabras, mostramos una alerta
      alert(`Error: La tarea debe tener al menos 3 palabras\nPalabras actuales: ${words.length}`);  
      return; // Salimos de la función si no cumple con el requisito
    }
    
    // 3. La tarea no puede exceder los 150 caracteres
    if (taskText.length > 150) { 
      alert(`Error: La tarea no puede tener más de 150 caracteres\nCaracteres actuales: ${taskText.length}`); 
      return; // Salimos de la función si excede el límite
    }
    
    // Si pasa todas las validaciones, llamamos la función que agrega la tarea
    onAddTask(taskText);
  };
  
  const handleChange = (e) => { // Esta función se ejecuta cuando el usuario escribe en el textarea
    setTaskText(e.target.value); // Actualizamos el estado con el valor actual del textarea que es pendiente o completada
  };
  
  // Cálculos para mostrar al usuario sobre la longitud de la tarea
  const charCount = taskText.length; // Contamos los caracteres
  const wordCount = taskText.trim().split(/\s+/).filter(word => word.length > 0).length; // Contamos las palabras válidas
  const isValid = wordCount >= 3 && charCount <= 150 && taskText.trim() !== ''; // Validamos si la tarea cumple con los requisitos
  
  return (
    <div className="task-form-modal"> 
      <div className="modal-header">  
        <h2>Nueva Tarea</h2>
        <button className="close-btn" onClick={onClose}>×</button>
      </div>
      {/* Formulario principal */}
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Descripción de la tarea:</label>
          <textarea
            value={taskText} // Valor controlado por el estado taskText
            onChange={handleChange} // Manejador de cambio para actualizar el estado
            placeholder="Ej: Examen del segundo parcial de Tecnologías Web II"
            rows="4"
            className="form-input"
            autoFocus
          />

         {/* Información dinámica: muestra palabras y caracteres en tiempo real */}
          <div className="form-info">
            <span className={wordCount < 3 ? 'text-warning' : ''}> {/* Si hay menos de 3 palabras, aplicamos una clase de advertencia */}
              📝 Palabras: {wordCount}/3 
            </span>
            <span className={charCount > 150 ? 'text-error' : ''}> {/* Si excede 150 caracteres, aplicamos una clase de error */}
              🔤 Caracteres: {charCount}/150
            </span>
          </div>
        </div>
        
        {/* Botones de acción del formulario */}
        <div className="form-actions">

          {/* Botón para cancelar la creación de la tarea */}
          <button 
            type="button" 
            className="btn btn-secondary"
            onClick={onClose}
          >
            Cancelar
          </button>

          {/* Botón para enviar el formulario*/}
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

export default TaskForm; // Exportamos el componente para usarlo en App.jsx