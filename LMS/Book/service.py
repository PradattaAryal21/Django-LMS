from .repositories import BookRepository

class BookService:
    def __init__(self):
        self.repository = BookRepository()

    def get_all_Books(self):
        return self.repository.get_all()

    def get_Book_by_id(self, Book_id):
        return self.repository.get_by_id(Book_id)

    def create_Book(self, data):
        return self.repository.create(data)

    def update_Book(self, Book_id, data):
        return self.repository.update(Book_id, data)

    def delete_Book(self, Book_id):
        return self.repository.delete(Book_id)
