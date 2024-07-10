from django.db import models
from django.contrib.auth.models import User
from .constrants import Ratings_choise
from django.utils.text import slugify
# Create your models here.







class Category(models.Model):
    category_name=models.CharField(max_length=100)
    slug=models.SlugField(max_length=100,unique=True,null=True,blank=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.category_name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.category_name
    


class Book(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='book/media/uploades/', blank=True, null=True)
    borrowing_price = models.DecimalField(max_digits=10, decimal_places=2)
    categories = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    def __str__(self):
        return self.title
    



class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review_text = models.TextField()
    rating = models.IntegerField(choices=Ratings_choise,null=True)

    def __str__(self):
        return f'Review of {self.book.title} by {self.user.username}'

