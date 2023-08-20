from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser,BlogPost

class CustomUserCreationForm(UserCreationForm):
    profile_picture = forms.ImageField(required=False)
    address_line1 = forms.CharField(max_length=255)
    city = forms.CharField(max_length=100)
    state = forms.CharField(max_length=100)
    pincode = forms.CharField(max_length=10)

    class Meta:
        model = CustomUser
        USER_TYPE_CHOICES = (
        ('patient', 'Patient'),
        ('doctor', 'Doctor'),
    )
    
        user_type = forms.ChoiceField(choices=USER_TYPE_CHOICES, widget=forms.RadioSelect)

        fields = ('username', 'first_name', 'last_name', 'email', 'profile_picture',
                  'address_line1', 'city', 'state', 'pincode', 'password1', 'password2','user_type')
class Blogpostform(forms.ModelForm):
    class Meta:
        model=BlogPost
        fields=['title','Image','content','Summary','Category','draft']