from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login,logout
from .forums import CustomUserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST,request.FILES)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Signup successful. You can now log in.')
            return redirect('login')  # Replace 'login' with your login URL
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    if field == 'password1' or field == 'password2':
                        messages.error(request, f'Invalid password: {error}')
                    else:
                        messages.error(request, f'Error in field {field}: {error}')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')  
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
@login_required
def dashboard(request):
    user = request.user
    if request.user.user_type=='doctor':
        patients=CustomUser.objects.filter(user_type='patient')
        return render(request,'dashboard.html',{'patients':patients})
    return render(request, 'dashboard.html', {'user': user})
def logout(request):
    return redirect('login')

