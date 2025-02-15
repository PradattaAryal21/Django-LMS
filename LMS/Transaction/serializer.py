from rest_framework import serializers
from .models import Transaction
from Student.models import Student
from Auth.models import User
from Book.models import Book

class TransactionSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source='student.name', read_only=True)
    librarian_name = serializers.CharField(source='user.user_name', read_only=True)
    book_name = serializers.CharField(source='book.title', read_only=True)

    class Meta:
        model = Transaction
        fields = ['transaction_id', 'student', 'user', 'book', 'transaction_type', 'date', 'student_name', 'librarian_name', 'book_name']
        read_only_fields = ['student_name', 'librarian_name', 'book_name']

