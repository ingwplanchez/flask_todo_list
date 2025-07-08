# flask_todo_list/app.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Base de datos de tareas (ya tiene id, content, completed) ---
tasks = []
next_task_id = 1

# --- Rutas de la Aplicación ---

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    global tasks
    global next_task_id

    if request.method == 'POST':
        task_content = request.form['content'].strip()
        if task_content:
            tasks.append({'id': next_task_id, 'content': task_content, 'completed': False})
            next_task_id += 1

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
            task['completed'] = not task['completed']
            break
    return redirect(url_for('index'))

# --- Nueva ruta para mostrar el formulario de edición ---
@app.route('/edit/<int:task_id>')
def edit_task(task_id):
    requested_task = None
    for task in tasks:
        if task['id'] == task_id:
            requested_task = task
            break
    if not requested_task:
        # Si la tarea no se encuentra, redirigir al inicio o mostrar un error
        return redirect(url_for('index'))
    return render_template('edit.html', task=requested_task)

# --- Nueva ruta para procesar el formulario de edición (POST) ---
@app.route('/update/<int:task_id>', methods=['POST'])
def update_task(task_id):
    global tasks
    if request.method == 'POST':
        updated_content = request.form['content'].strip()
        if updated_content:
            for task in tasks:
                if task['id'] == task_id:
                    task['content'] = updated_content # Actualiza el contenido de la tarea
                    break
    return redirect(url_for('index'))

# --- Ejecutar la Aplicación ---
if __name__ == '__main__':
    app.run(debug=True)