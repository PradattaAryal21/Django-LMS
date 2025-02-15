from .repositories import AuthorRepository

class AuthorService:
    @staticmethod
    def get_all_authors():
        return AuthorRepository.get_all()

    @staticmethod
    def get_author_by_id(author_id):
        return AuthorRepository.get_by_id(author_id)

    @staticmethod
    def create_author(author_data):
        return AuthorRepository.create(author_data)

    @staticmethod
    def update_author(author_id, author_data):
        author = AuthorRepository.get_by_id(author_id)
        if author:
            return AuthorRepository.update(author, author_data)
        return None

    @staticmethod
    def delete_author(author_id):
        author = AuthorRepository.get_by_id(author_id)
        if author:
            AuthorRepository.delete(author)
            return True
        return False