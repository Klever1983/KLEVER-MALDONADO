# Sistema de Gestión de Biblioteca Digital

Este proyecto implementa un sistema de gestión para una biblioteca digital en **Python**, aplicando Programación Orientada a Objetos (POO) y colecciones como listas, diccionarios, tuplas y conjuntos.

## Funcionalidades
- **Gestión de libros**: añadir, eliminar, buscar por título, autor o categoría.
- **Gestión de usuarios**: registrar y dar de baja usuarios.
- **Préstamos**: prestar y devolver libros.
- **Listados**: libros disponibles, prestados y préstamos de cada usuario.

## Estructura del proyecto
```
library_system/
├── library.py   # Clases principales (Book, User, Library)
├── tests.py     # Script de pruebas y demostración
└── README.md    # Documentación del proyecto
```

## Ejecución
```bash
python tests.py
```

Esto mostrará ejemplos de creación de libros, registro de usuarios, préstamos y búsquedas.

## Subir a GitHub
1. Crear un repositorio público en GitHub.
2. Desde la carpeta del proyecto:
```bash
git init
git add .
git commit -m "Entrega: Sistema de Gestión de Biblioteca Digital"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/NOMBRE_REPO.git
git push -u origin main
```
