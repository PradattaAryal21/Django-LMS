from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['book_id', 'title', 'author', 'genre', 'isbn', 'quantity']

    def validate_quantity(self, value):
        """Validate the quantity field."""
        if value < 0:
            raise serializers.ValidationError("Quantity cannot be negative.")
        return value