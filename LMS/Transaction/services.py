from .repositories import TransactionRepository

class TransactionService:
    def __init__(self):
        self.repository = TransactionRepository()

    def list_transactions(self):
        return self.repository.get_all()

    def get_transaction(self, transaction_id):
        return self.repository.get_by_id(transaction_id)

    def create_transaction(self, data):
        return self.repository.create(data)

    def update_transaction(self, transaction_id, data):
        return self.repository.update(transaction_id, data)

    def delete_transaction(self, transaction_id):
        return self.repository.delete(transaction_id)
