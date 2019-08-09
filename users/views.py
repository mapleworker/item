from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm
from django.contrib.auth.models import User
from django.contrib import auth
def logout_view(request):
    """Log the user out."""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.   
        form = UserCreationForm()
    else:
        # Process completed form.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password2']
            new_user = User.objects.create_user(username=username, password=password)
            #new_user = form.save()
            # Log the user in, and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username,
                password=request.POST['password1'])
            auth.login(request, authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))

    context = {'form': form}
    return render(request, 'users/register.html', context)




def login(request):
    if request.method == "POST":
        login_form = UserForm(request.POST)
        message = "请检查填写的内容！"
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            try:
                user = authenticate(username=username,password=password)
                if user is not None and user.is_active:
                    auth.login(request, user)
                    return HttpResponseRedirect(reverse('learning_logs:index'))
                else:
                    message = "密码不正确！"
            except:
                message = "用户不存在！"
        return render(request, 'users/login.html', locals())
 
    login_form = UserForm()
    return render(request, 'users/login.html', locals())
