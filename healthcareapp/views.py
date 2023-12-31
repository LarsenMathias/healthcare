from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import login,logout
from .forums import CustomUserCreationForm,Blogpostform
from django.contrib.auth.forms import AuthenticationForm
from .models import CustomUser,BlogPost,Category
from django.shortcuts import get_object_or_404
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
def dashboard(request):
    user = request.user
    if not request.user.is_authenticated:
        return redirect('login')
    if request.user.user_type=='doctor':
        patients=CustomUser.objects.filter(user_type='patient')
        return render(request,'dashboard.html',{'patients':patients})
    return render(request, 'dashboard.html', {'user': user})
def logout(request):
    request.session.flush()
    return redirect('login')
def blogpost(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category_id')
    if category_id:
        posts = BlogPost.objects.filter(Category__id=category_id, draft='upload')
    else:
        posts = BlogPost.objects.filter(draft='upload')

    data = {
        'categories': categories,
        'posts': posts,
    }
    return render(request, 'blogpost.html', data)

def blog_detail(request,post_id):
    post= get_object_or_404(BlogPost, pk=post_id)
    return render(request,'blog_detail.html',{'post':post})
def upload_blog(request):
    if request.method == 'POST':
        form = Blogpostform(request.POST, request.FILES)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user 
            blog_post.save()
            return redirect('blogpost')
    else:
        form = Blogpostform()
    
    return render(request, 'upload_blog.html', {'form': form})