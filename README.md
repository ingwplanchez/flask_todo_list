# flask\_todo\_list: Un Sencillo Gestor de Tareas con Flask

## Descripción del Proyecto

`flask_todo_list` es una aplicación web minimalista diseñada para ayudarte a gestionar tus tareas diarias. Permite añadir, listar, marcar como completadas, editar y eliminar tareas de forma sencilla. El proyecto está construido utilizando el microframework **Flask** para el backend y una interfaz de usuario básica para el frontend.

Este repositorio documenta el progreso del desarrollo de la aplicación, siguiendo una serie de pasos que construyen la funcionalidad gradualmente.

## Características y Funcionalidades

Hasta el momento, `flask_todo_list` incluye las siguientes características clave:

  * **Gestión Básica de Tareas (CRUD):**
      * **Crear:** Añade nuevas tareas a tu lista.
      * **Leer:** Visualiza todas tus tareas pendientes y completadas.
      * **Actualizar:**
          * **Marcar como Completadas:** Cambia el estado de una tarea a "completada" con un solo clic, tachando su texto para una clara distinción visual.
          * **Editar:** Modifica el contenido de una tarea existente.
      * **Eliminar:** Borra tareas de forma permanente de la lista.
  * **Base de Datos Ligera:** Utiliza SQLite para almacenar las tareas de forma local, proporcionando una solución de persistencia simple y eficaz.

## Tecnologías Utilizadas

  * **Backend:**
      * Python 3
      * Flask
      * SQLAlchemy (ORM para la interacción con la base de datos)
  * **Frontend:**
      * HTML5
      * CSS (estilos básicos)
      * JavaScript (para interacciones sencillas)

## Pasos de Desarrollo Implementados

Este proyecto ha sido desarrollado siguiendo los siguientes hitos:

### Paso 1: Configuración Inicial del Proyecto

Se estableció la estructura básica del proyecto Flask, incluyendo la configuración inicial del entorno y los archivos esenciales.

### Paso 2: Estructura Básica de la Aplicación Flask

Se creó el archivo principal de la aplicación (`app.py`), se definió el modelo de la base de datos para las tareas y se configuraron las rutas básicas para mostrar la lista de tareas y añadir nuevas.

### Paso 3: Ejecutar la Aplicación

Se implementaron las instrucciones para ejecutar la aplicación Flask localmente, permitiendo visualizar la interfaz inicial y probar la adición de tareas.

### Paso 4: Añadir Funcionalidad para Eliminar Tareas

Se integró la lógica en el backend y los enlaces en el frontend para permitir a los usuarios eliminar tareas de la lista.

### Paso 5: Probar la Funcionalidad de Eliminación

Se realizaron pruebas para asegurar que la eliminación de tareas funcionara correctamente, tanto a nivel de interfaz como de persistencia en la base de datos.

### Paso 6: Añadir Funcionalidad para Marcar Tareas como Completadas

Se añadió la capacidad de alternar el estado de una tarea entre "pendiente" y "completada", actualizando su apariencia visual en la interfaz.

### Paso 7: Añadir Funcionalidad para Editar Tareas

Se implementó la ruta y la lógica necesarias para permitir a los usuarios editar el contenido de una tarea existente directamente desde la interfaz.

## Cómo Ejecutar el Proyecto Localmente

Para poner en marcha `flask_todo_list` en tu máquina, sigue estas instrucciones:

1.  **Clona el repositorio:**

    ```bash
    git clone https://github.com/tu-usuario/flask_todo_list.git
    cd flask_todo_list
    ```

    (Asegúrate de reemplazar `tu-usuario/flask_todo_list.git` con la URL real de tu repositorio).

2.  **Crea un entorno virtual (recomendado):**

    ```bash
    python -m venv venv
    ```

3.  **Activa el entorno virtual:**

      * En Windows (CMD):
        ```bash
        .\venv\Scripts\activate
        ```
      * En macOS/Linux/Git Bash:
        ```bash
        source venv/bin/activate
        ```

4.  **Instala las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

    (Asegúrate de tener un archivo `requirements.txt` en la raíz de tu proyecto con `Flask` y `Flask-SQLAlchemy` listados).

5.  **Inicializa la base de datos:**

    ```bash
    python -c "from app import db; db.create_all()"
    ```

    (Este comando asume que tu archivo principal de Flask se llama `app.py` y que el objeto `db` de SQLAlchemy está definido en él).

6.  **Ejecuta la aplicación:**

    ```bash
    flask run
    ```

    Si tu archivo principal de Flask no se llama `app.py`, necesitarás establecer la variable de entorno `FLASK_APP` antes de `flask run`:

      * En Windows (CMD):
        ```bash
        set FLASK_APP=app.py
        flask run
        ```
      * En Windows (PowerShell):
        ```powershell
        $env:FLASK_APP="app.py"
        flask run
        ```
      * En macOS/Linux/Git Bash:
        ```bash
        export FLASK_APP=app.py
        flask run
        ```

7.  **Accede a la aplicación:**
    Abre tu navegador web y ve a `http://127.0.0.1:5000/`.

## Estructura del Proyecto (Ejemplo Típico)

```
flask_todo_list/
├── venv/                   # Entorno virtual de Python
├── app.py                  # Archivo principal de la aplicación Flask
├── requirements.txt        # Lista de dependencias de Python
├── instance/               # Carpeta para archivos de instancia (ej. base de datos SQLite)
│   └── todo.db             # Nombre de tu archivo de base de datos
├── templates/
│   ├── index.html          # Plantilla principal de la aplicación
│   └── edit.html           # Plantilla para la edición de tareas (o similar)
└── static/
    ├── css/
    │   └── style.css       # Archivos CSS personalizados
    └── js/                 # Carpeta para archivos JavaScript
        └── script.js
```


