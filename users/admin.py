from django.contrib import admin
from .models import UserProfile,BorrowedBook
# Register your models here.

admin.site.register(UserProfile)
admin.site.register(BorrowedBook)