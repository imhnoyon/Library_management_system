from django.contrib import admin
from .models import Book,Review,Category
# Register your models here.
admin.site.register(Book)
admin.site.register(Review)

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ('category_name',)}
    list_display = ['category_name', 'slug']
    
admin.site.register(Category, CategoryAdmin)




