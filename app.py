# flask_todo_list/app.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Base de datos de tareas (por ahora, una lista simple en memoria) ---
# En un proyecto real, usarías una base de datos como SQLite, PostgreSQL, etc.
# Pero para empezar, esto es perfecto.
tasks = [] # Lista para almacenar las tareas

# --- Rutas de la Aplicación ---

@app.route('/')
def index():
    # Esta ruta mostrará la página principal con la lista de tareas.
    return render_template('index.html', tasks=tasks) # Pasamos la lista de tareas a la plantilla

@app.route('/add', methods=['POST'])
def add_task():
    # Esta ruta manejará la adición de nuevas tareas.
    # Solo acepta solicitudes POST (cuando se envía un formulario).
    if request.method == 'POST':
        task_content = request.form['content'] # Obtiene el contenido de la tarea del formulario
        if task_content: # Asegúrate de que el campo no esté vacío
            tasks.append(task_content) # Añade la tarea a nuestra lista

    return redirect(url_for('index')) # Redirige de vuelta a la página principal para ver la tarea añadida

# --- Ejecutar la Aplicación ---
if __name__ == '__main__':
    app.run(debug=True) # debug=True permite recargar automáticamente el servidor en cambios y ver errores