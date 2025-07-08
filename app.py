# flask_todo_list/app.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Base de datos de tareas (ahora con campo 'completed') ---
# Cada tarea es un diccionario: {'id': 1, 'content': 'Aprender Flask', 'completed': False}
tasks = []
next_task_id = 1 # Usaremos esto para asegurar que los IDs sean únicos y crecientes.

# --- Rutas de la Aplicación ---

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    global tasks
    global next_task_id # Necesitamos acceder a esta variable global para incrementarla

    if request.method == 'POST':
        task_content = request.form['content'].strip()
        if task_content:
            tasks.append({'id': next_task_id, 'content': task_content, 'completed': False})
            next_task_id += 1 # Incrementamos el ID para la próxima tarea

    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete_task(task_id):
    global tasks
    for task in tasks:
        if task['id'] == task_id:
            task['completed'] = not task['completed'] # Alterna el estado (True a False, False a True)
            break # Una vez que encontramos la tarea, podemos salir del bucle
    return redirect(url_for('index'))

# --- Ejecutar la Aplicación ---
if __name__ == '__main__':
    app.run(debug=True)