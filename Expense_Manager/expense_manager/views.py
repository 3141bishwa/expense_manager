from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_auth

def home(request):
    if request.user.is_authenticated():
        return render(request, 'expense_manager/dashboard.html')
    
    else:
        return render(request, 'expense_manager/home.html')
    
def signup(request):
    if request.method == 'POST':
        userName = request.POST['name']
        if User.objects.filter(username = userName).exists():
            return render(request, 'expense_manager/signup.html', {'message' : 'You are already a user. Please proceed to the login'})

        password = request.POST['password']
        emailAddress = request.POST['email_address']
        newUser = User.objects.create_user(userName, emailAddress, password)
        newUser.save()
        user = authenticate(username = userName, password = password)
        login_auth(request, user)
        return render(request, 'expense_manager/dashboard.html')
    
    return render(request, 'expense_manager/signup.html')

def login(request):
    user_name = request.POST['name']
    password = request.POST['password']
    user = authenticate(username = user_name, password = password)
    
    if user is not None:
        login_auth(request, user)
        return render(request, 'expense_manager/dashboard.html')
    else:
        return render(request, 'expense_manager/home.html' , {'message' : "Sorry, the given username and password don't seem to match. Please try again"})

def logout_view(request):
    logout(request)
    return render(request, 'expense_manager/home.html', {'message' : 'You have successfully logged out of the application'})