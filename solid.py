import logging
from abc import ABC, abstractmethod

# Налаштування логування
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class Book:
    def __init__(self, title: str, author: str, year: int):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"


class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book):
        pass

    @abstractmethod
    def remove_book(self, title: str):
        pass

    @abstractmethod
    def show_books(self):
        pass


class Library(LibraryInterface):
    def __init__(self):
        self.books = []

    def add_book(self, book: Book):
        self.books.append(book)
        logging.info(f"Book added: {book}")

    def remove_book(self, title: str):
        original_count = len(self.books)
        self.books = [book for book in self.books if book.title != title]
        if len(self.books) < original_count:
            logging.info(f"Book removed: {title}")
        else:
            logging.info(f"Book not found: {title}")

    def show_books(self):
        if not self.books:
            logging.info("No books in the library.")
        else:
            for book in self.books:
                logging.info(book)


class LibraryManager:
    """Клас для управління бібліотекою через абстракцію."""

    def __init__(self, library: LibraryInterface):
        self.library = library

    def add_book(self, title: str, author: str, year: int):
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str):
        self.library.remove_book(title)

    def show_books(self):
        self.library.show_books()


def main():
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                try:
                    year = int(input("Enter book year: ").strip())
                    manager.add_book(title, author, year)
                except ValueError:
                    logging.warning("Invalid year format. Please enter a number.")
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                logging.info("Exiting the program.")
                break
            case _:
                logging.warning("Invalid command. Please try again.")


if __name__ == "__main__":
    main()
