from .repositories import BookRepository

class BookService:
    def __init__(self):
        self.repository = BookRepository()  # Instance of Repository

    def get_all_books(self):
        return self.repository.get_all()

    def get_book_by_id(self, book_id):
        return self.repository.get_by_id(book_id)

    def create_book(self, book_data):
        return self.repository.create(book_data)

    def update_book(self, book_id, book_data):
        book = self.repository.get_by_id(book_id)
        if book:
            return self.repository.update(book, book_data)
        return None

    def delete_book(self, book_id):
        book = self.repository.get_by_id(book_id)
        if book:
            self.repository.delete(book)
            return True
        return False
