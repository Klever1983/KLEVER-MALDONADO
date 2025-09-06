# tests.py
# Demostración del sistema de gestión de biblioteca digital

from library import Library

lib = Library()

# Crear libros
lib.add_book("Cien años de soledad", "Gabriel García Márquez", "978-0307474728", "Novela")
lib.add_book("El Principito", "Antoine de Saint-Exupéry", "978-0156012195", "Infantil")
lib.add_book("Python para todos", "Raúl González", "978-1234567890", "Programación")

# Registrar usuarios
lib.register_user("Ana Pérez", "U001")
lib.register_user("Juan López", "U002")

# Prestar libros
print("Préstamo exitoso:", lib.lend_book("978-0307474728", "U001"))

# Buscar libros
print("Buscar 'Python':", lib.search_by_title("Python"))

# Listar préstamos de un usuario
print("Libros prestados a U001:", lib.list_user_loans("U001"))

# Devolver libro
print("Devolución exitosa:", lib.return_book("978-0307474728", "U001"))

# Estado final
print("Estado final de la biblioteca:", lib)
