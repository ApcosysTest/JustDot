from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model
from django import forms
from .models import *

# Register Form
class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')

# Login Form
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')

CHOICES = [
    ('Mr', 'Mr'),
    ('Ms', 'Ms'),
    ('Dr', 'Dr'),
]
# Personal Form
class PersonalForm(forms.ModelForm):
    title = forms.ChoiceField(widget=forms.RadioSelect,choices=CHOICES)
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'E.g. Shruti'}))
    middle_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'E.g. Ramesh'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'E.g. Tendulkar'}))
    dob = forms.DateField(widget=forms.DateInput(format=('%d-%m-%Y'),attrs={'class': 'datepicker','type': 'date'}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'E.g. 708, Barton Center'}))
    city = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'E.g. Bengaluru'}))
    state = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'E.g. Karnataka'}))
    pincode = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'E.g. 560001'}))
    mobile_number = forms.IntegerField(widget=forms.TextInput(attrs={'placeholder':'E.g. 9135200117'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'placeholder':'E.g. shruti94@gmail.com'}))
    about = forms.CharField(widget=forms.Textarea(attrs=({'placeholder':'E.g. I am a self-taught developer who loves to solve problems digitally with top notch technologies. I am specialized in web technologies. I am working to learn new technologies and seize new opportunities as well as develop creative ideas.',})))
    
    class Meta:
        model = Personal
        fields = ('title','first_name','middle_name','last_name','dob','photo','address','city','state','pincode','mobile_number','email','about')