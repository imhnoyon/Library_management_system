from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Category, Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required
from users.models import BorrowedBook
from users.models import UserProfile
from django.contrib import messages
from users.views import send_transaction_email

def book_list(request,category_slug=None):
    books = Book.objects.all()
    if category_slug :
        category=Category.objects.get(slug=category_slug)
        books=Book.objects.filter(categories=category)

    category_list=Category.objects.all()
    return render(request, 'books/book_list.html', {'books': books, 'categories': category_list})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    reviews = Review.objects.filter(book=book)
    return render(request, 'books/book_detail.html', {'book': book, 'reviews': reviews})

@login_required
def borrow_book(request, pk):
    book=Book.objects.get(pk=pk)
    user_profile=UserProfile.objects.get(user=request.user)
    if user_profile.balance >= book.borrowing_price:
        user_profile.balance -= book.borrowing_price
        user_profile.save()
        BorrowedBook.objects.create(user=request.user, book=book)
        send_transaction_email(request.user,user_profile,book.borrowing_price,'Book purcharse',"books/book_purchase.html")
        return redirect('user_profile')
    else:
        messages.error(request,'You have not enough money')

    return redirect('Homepages')

     
     




@login_required
def return_book(request, pk):
    borrowed_book = get_object_or_404(BorrowedBook, pk=pk, user=request.user, returned=False)
    user_profile = request.user.userprofile
    user_profile.balance += borrowed_book.book.borrowing_price
    user_profile.save()
    borrowed_book.returned = True
    borrowed_book.save()
    send_transaction_email(request.user,user_profile,borrowed_book.book.borrowing_price,'Returned book',"books/return_book.html")
    return redirect('Homepages')

@login_required
def review_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.book = book
            review.user = request.user
            review.save()
            return redirect('book_details', pk=book.pk)
    else:
        form = ReviewForm()
    return render(request, 'books/review_book.html', {'form': form})









