from django.db import models
from django.contrib.auth.models import User
from books.models import Book
# Create your models here.

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    balance=models.DecimalField(max_digits=12, decimal_places=2, default=0.0)
    def __str__(self):
        return str(int(self.balance))


class BorrowedBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField(auto_now_add=True)
    returned = models.BooleanField(default=False)

    def __str__(self):
        return self.book.title
    


