from .repositories import TransactionRepository

class TransactionService:
    def __init__(self):
        self.repository = TransactionRepository()

    def get_all_Transactions(self):
        return self.repository.get_all()

    def get_Transaction_by_id(self, transaction_id):
        return self.repository.get_by_id(transaction_id)

    def create_Transaction(self, data):
        return self.repository.create(data)

    def update_Transaction(self, transaction_id, data):
        return self.repository.update(transaction_id, data)

    def delete_Transaction(self, transaction_id):
        return self.repository.delete(transaction_id)
