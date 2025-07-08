# flask_todo_list/app.py

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# --- Base de datos de tareas (ahora con un identificador único si lo necesitamos más adelante) ---
# Vamos a almacenar las tareas como diccionarios para que cada una tenga un ID único.
# Esto es más robusto que usar el índice de la lista, especialmente si las tareas se reordenan o eliminan.
# current_id = 0 # Puedes inicializarlo aquí si quieres auto-incrementar IDs.
tasks = [] # Lista para almacenar diccionarios de tareas, por ejemplo: [{'id': 1, 'content': 'Aprender Flask'}]

# --- Rutas de la Aplicación ---

@app.route('/')
def index():
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add_task():
    global tasks # Declara que vamos a modificar la variable global tasks
    # No necesitamos 'global current_id' si vamos a usar len(tasks)
    if request.method == 'POST':
        task_content = request.form['content'].strip() # .strip() para quitar espacios en blanco al inicio/final
        if task_content:
            # Asignamos un ID. Una forma sencilla para este ejemplo es usar el tamaño actual de la lista + 1
            # Para un sistema más robusto con IDs únicos y persistentes, se usaría una base de datos.
            new_id = len(tasks) + 1 # Asignamos el ID basado en el tamaño actual de la lista.
                                     # Nota: si borras elementos, los IDs podrían no ser secuenciales.
                                     # Para un ID realmente único y que no se repita nunca, se usaría UUID o una base de datos.
                                     # Pero para este ejercicio, es funcional.
            tasks.append({'id': new_id, 'content': task_content})

    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    global tasks # Declara que vamos a modificar la variable global tasks
    # Crea una nueva lista excluyendo la tarea con el ID coincidente
    # Esta es una forma segura de eliminar elementos de una lista mientras se itera
    tasks = [task for task in tasks if task['id'] != task_id]
    return redirect(url_for('index'))

# --- Ejecutar la Aplicación ---
if __name__ == '__main__':
    app.run(debug=True)