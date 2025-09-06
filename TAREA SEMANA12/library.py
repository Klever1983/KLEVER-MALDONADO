# library.py
# Sistema de Gestión de Biblioteca Digital

from dataclasses import dataclass
from typing import Tuple, List, Dict, Set, Optional

@dataclass(frozen=True)
class Book:
    """Representa un libro con atributos inmutables (título y autor en tupla)."""
    _meta: Tuple[str, str]  # (title, author)
    isbn: str
    category: str

    @property
    def title(self) -> str:
        return self._meta[0]

    @property
    def author(self) -> str:
        return self._meta[1]

    def __repr__(self) -> str:
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}', category='{self.category}')"


class User:
    """Representa un usuario de la biblioteca."""
    def __init__(self, name: str, user_id: str):
        self.name = name
        self.user_id = user_id
        self.borrowed: List[str] = []

    def borrow(self, isbn: str) -> None:
        if isbn not in self.borrowed:
            self.borrowed.append(isbn)

    def give_back(self, isbn: str) -> None:
        if isbn in self.borrowed:
            self.borrowed.remove(isbn)

    def list_borrowed(self) -> List[str]:
        return list(self.borrowed)

    def __repr__(self) -> str:
        return f"User(name='{self.name}', user_id='{self.user_id}', borrowed={self.borrowed})"


class Library:
    """Gestiona libros, usuarios y préstamos."""
    def __init__(self):
        self.books: Dict[str, Book] = {}
        self.users: Dict[str, User] = {}
        self.user_ids: Set[str] = set()
        self.loans: Dict[str, str] = {}  # isbn -> user_id

    # --- Gestión de libros ---
    def add_book(self, title: str, author: str, isbn: str, category: str) -> bool:
        if isbn in self.books:
            return False
        self.books[isbn] = Book(_meta=(title, author), isbn=isbn, category=category)
        return True

    def remove_book(self, isbn: str) -> bool:
        if isbn not in self.books or isbn in self.loans:
            return False
        del self.books[isbn]
        return True

    # --- Gestión de usuarios ---
    def register_user(self, name: str, user_id: str) -> bool:
        if user_id in self.user_ids:
            return False
        self.users[user_id] = User(name, user_id)
        self.user_ids.add(user_id)
        return True

    def deregister_user(self, user_id: str) -> bool:
        if user_id not in self.user_ids:
            return False
        if self.users[user_id].borrowed:
            return False
        del self.users[user_id]
        self.user_ids.remove(user_id)
        return True

    # --- Préstamos ---
    def lend_book(self, isbn: str, user_id: str) -> bool:
        if isbn not in self.books or user_id not in self.user_ids:
            return False
        if isbn in self.loans:
            return False
        self.loans[isbn] = user_id
        self.users[user_id].borrow(isbn)
        return True

    def return_book(self, isbn: str, user_id: str) -> bool:
        if isbn not in self.loans or self.loans[isbn] != user_id:
            return False
        del self.loans[isbn]
        self.users[user_id].give_back(isbn)
        return True

    # --- Búsquedas ---
    def search_by_title(self, query: str) -> List[Book]:
        return [b for b in self.books.values() if query.lower() in b.title.lower()]

    def search_by_author(self, query: str) -> List[Book]:
        return [b for b in self.books.values() if query.lower() in b.author.lower()]

    def search_by_category(self, category: str) -> List[Book]:
        return [b for b in self.books.values() if category.lower() == b.category.lower()]

    # --- Listados ---
    def list_user_loans(self, user_id: str) -> Optional[List[Book]]:
        if user_id not in self.user_ids:
            return None
        return [self.books[isbn] for isbn in self.users[user_id].borrowed]

    def list_all_books(self) -> List[Book]:
        return list(self.books.values())

    def list_available_books(self) -> List[Book]:
        return [b for isbn, b in self.books.items() if isbn not in self.loans]

    def list_loaned_books(self) -> List[Book]:
        return [self.books[isbn] for isbn in self.loans.keys()]

    def __repr__(self) -> str:
        return f"Library(books={len(self.books)}, users={len(self.users)}, loans={len(self.loans)})"
