from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from .forms import UserRegisterForm, DepositForm
from .models import UserProfile, BorrowedBook
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.template.loader import render_to_string
from django.core.mail import EmailMessage,EmailMultiAlternatives

def send_transaction_email(user,user_profile, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
            'user_profile':user_profile
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()







def Register(request):
    print('login')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login') 
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})



def user_login(request):
    if request.method=='POST':
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            user_name=form.cleaned_data['username']
            user_pass=form.cleaned_data['password']
            user=authenticate(username=user_name,password=user_pass)
            if user is not None:
                login(request,user)
                return redirect('user_profile')
        else:
            return redirect('login')
            
    else:
        form=AuthenticationForm()
    return render(request,'users/login.html',{'form':form})




@login_required
def deposit_money(request):
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            user_profile=UserProfile.objects.get(user=request.user)
            depost_amount=form.cleaned_data['amount']
            print(user_profile)
            user_profile.balance +=depost_amount
            user_profile.save(update_fields=['balance'])
            messages.success(request,'Deposit Successfully')
           
            send_transaction_email(request.user,user_profile,depost_amount,'Deposit','users/diposit_money_email.html')

            return redirect('user_profile')
    else:
        form = DepositForm()
    return render(request, 'users/deposit_money.html', {'form': form})


from .models import UserProfile
@login_required
def user_profile(request):
    borrowed_books = BorrowedBook.objects.filter(user=request.user,returned=False)
    # deposits = UserProfile.objects.filter(user=request.user)
    deposits, created = UserProfile.objects.get_or_create(user=request.user)
    # deposits=UserProfile.objects.get(user=request.user)
    return render(request, 'users/profile.html', {'borrowed_books': borrowed_books,'Balance':deposits})



def User_logout(request):
    logout(request)
    return redirect('login')