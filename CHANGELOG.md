# 📒 Changelog

Todas las versiones relevantes del proyecto se listan aquí. Este archivo sigue el formato [Keep a Changelog](https://keepachangelog.com/es/1.0.0/) y la convención de versionado semántico: `MAJOR.MINOR.PATCH`.

---

## [v2.0.0] - 2025-07-09

### 🔄 Cambiado
- Migración de almacenamiento en diccionario hacia una base de datos con SQLAlchemy
- Se actualizaron las rutas para interactuar con el modelo `Tarea`

### ➕ Añadido
- Modelo `Tarea` con campos: `id`, `titulo`, `completada`
- Configuración de SQLite como motor local
- Integración de Flask-SQLAlchemy en el proyecto

---

## [v1.0.0] - 2025-07-08

### 🎉 Lanzamiento inicial
- Aplicación Flask básica para gestionar tareas
- Funcionalidad para agregar, editar, eliminar y marcar tareas como completadas
- Almacenamiento en diccionario en memoria

---

