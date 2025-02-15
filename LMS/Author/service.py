from .repositories import AuthorRepository

class AuthorService:
    def __init__(self):
        self.repository = AuthorRepository()

    def get_all_authors(self):
        return self.repository.get_all()

    def get_author_by_id(self, author_id):
        return self.repository.get_by_id(author_id)

    def create_author(self, data):
        return self.repository.create(data)

    def update_author(self, author_id, data):
        return self.repository.update(author_id, data)

    def delete_author(self, author_id):
        return self.repository.delete(author_id)
