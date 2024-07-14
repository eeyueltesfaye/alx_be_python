class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        return not self._is_checked_out

class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: {title}")
                return
        print(f"Book '{title}' is not available for checkout.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: {title}")
                return
        print(f"Book '{title}' was not checked out.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if not available_books:
            print("No books available.")
        for book in available_books:
            print(f"{book.title} by {book.author}")

# For testing within the script (you can remove this part when using main.py)
if __name__ == "__main__":
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))
    library.list_available_books()
    library.check_out_book("1984")
    library.list_available_books()
    library.return_book("1984")
    library.list_available_books()
