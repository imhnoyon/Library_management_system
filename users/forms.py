from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class UserRegisterForm(UserCreationForm):
    first_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))
    last_name=forms.CharField(widget=forms.TextInput(attrs={'id':'required'}))

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']

class DepositForm(forms.ModelForm):
    amount = forms.DecimalField(max_digits=12, decimal_places=2)
    class Meta:
        model = UserProfile
        fields = ['amount']
