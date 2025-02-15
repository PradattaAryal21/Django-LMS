from .models import Author

class AuthorRepository:
    def __init__(self):
        self.model = Author

    def get_all(self):
        return self.model.objects.all()

    def get_by_id(self, author_id):
        return self.model.objects.filter(author_id=author_id).first()

    def create(self, data):
        return self.model.objects.create(**data)

    def update(self, author_id, data):
        author = self.get_by_id(author_id)
        if author:
            for key, value in data.items():
                setattr(author, key, value)
            author.save()
        return author

    def delete(self, author_id):
        author = self.get_by_id(author_id)
        if author:
            author.delete()
            return True
        return False
