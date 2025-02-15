from django.db import models
from Author.models import Author
class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    genre = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13, unique=True)
    quantity = models.IntegerField()

    def __str__(self):
        return self.title
