from django.urls import path
from . import views
urlpatterns = [
    path('', views.book_list, name='Homepages'),
    path('category/<slug:category_slug>/', views.book_list, name='books_list'),
    path('books/<int:pk>/', views.book_detail, name='book_details'),
    path('borrow/<int:pk>', views.borrow_book, name='borrow_book'),
    path('books/<int:pk>/return/', views.return_book, name='return_book'),
    path('books/<int:pk>/review/', views.review_book, name='review_book'),
]

