from .models import Book

class BookRepository:
    def __init__(self):
        self.model = Book

    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, Book_id):
        return self.model.objects.filter(Book_id=Book_id).first()

    def create(self, data):
        return self.model.objects.create(**data)

    def update(self, Book_id, data):
        Book = self.get_by_id(Book_id)
        if Book:
            for key, value in data.items():
                setattr(Book, key, value)
            Book.save()
        return Book

    def delete(self, Book_id):
        Book = self.get_by_id(Book_id)
        if Book:
            Book.delete()
            return True
        return False
