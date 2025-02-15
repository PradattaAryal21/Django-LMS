from .models import Author

class AuthorRepository:
    @staticmethod
    def get_all():
        return Author.objects.all()

    @staticmethod
    def get_by_id(author_id):
        try:
            return Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return None

    @staticmethod
    def create(author_data):
        return Author.objects.create(**author_data)

    @staticmethod
    def update(author, author_data):
        for key, value in author_data.items():
            setattr(author, key, value)
        author.save()
        return author

    @staticmethod
    def delete(author):
        author.delete()