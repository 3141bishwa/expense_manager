from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as login_auth
from django.http import JsonResponse
import json
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse
from .models import UserExpense
from django.core import serializers
from django.views.decorators.clickjacking import xframe_options_exempt

# Renders the Home Page of the Application. If the user is signed in, redirects to the user's dashboard
def home(request):
    if request.user.is_authenticated():
        return render(request, 'expense_manager/dashboard.html')
    
    else:
        return render(request, 'expense_manager/home.html')

# View to process the signup page of the app
def signup(request):
    # Adds a previously non-existing user to the database if a POST request is made to the URL
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
        return redirect(request, 'expense_manager/dashboard.html')
    
    # Renders the page to signup else.
    return render(request, 'expense_manager/signup.html')

# View to authenticate Users
def login(request):
    user_name = request.POST['name']
    password = request.POST['password']
    user = authenticate(username = user_name, password = password)
    
    if user is not None:
        login_auth(request, user)
        return redirect('expense_manager.views.home')
    else:
        return render(request, 'expense_manager/home.html' , {'message' : "Sorry, the given username and password don't seem to match. Please try again"})

# View to logout
def logout_view(request):
    logout(request)
    return render(request, 'expense_manager/home.html', {'message' : 'You have successfully logged out of the application'})

# Returns all the users as a Json response for the dashboard
def getallusers(request):
    users = []
    
    for x in User.objects.all():
        users.append(x.username)

    return JsonResponse({'users': json.dumps(users)})

# Updates a new purchase that took place
@require_http_methods(["POST"])
def update_expense(request):
    expense_poster =  request.user.username
    # Gets all the users to whom the purchase is to be shared amongst
    myList = request.POST.getlist('checks')
    noOfShares = len(myList)
    individualShare = round(float(request.POST['amount'])/noOfShares,2)
    detail = request.POST['details']
    venue = request.POST['venue']
    
    for user in myList:
        newUpdate = UserExpense(expense_poster=expense_poster, username=user, cost=individualShare, description=detail, purchase_store=venue)
        newUpdate.save()
    return render(request, 'expense_manager/dashboard.html', {'message' : 'You have successfully recorded a purchase.'})

# Renders the following responses based on the request:
# if 'payable' is a parameter in the request, renders a page which gives the amount payable by the user to other users in the database
# if 'recent' is a parameter in the request, renders a page which gives two most recent expenses for the user
# if nothing, renders all the expenses for the user.
# The two most recent expenses are meant to be rendered on the dashboard itself inside an iframe while the page for all the expenses are for a separate URL
@xframe_options_exempt
def get_expenses(request):
    username=request.user.username
    
    # Gives a list of all expenses of the User
    myExpenses = list(UserExpense.objects.filter(username=username))
    
    # Only chooses the transactions not recorded by the given user since he/she wont have to make pay his/her own share.
    if 'payable' in request.GET:
        myDict = {}
        for expense in myExpenses:
            if expense.expense_poster!=username:
                if expense.expense_poster not in myDict:
                    myDict[expense.expense_poster]  = expense.cost
                else:
                    myDict[expense.expense_poster] += expense.cost
        
        return render(request, 'expense_manager/payable.html', {'expenses' : myDict})
    
    if 'recent' in request.GET:
        recentExpenses = []
        recentExpenses.append(myExpenses.pop())
        recentExpenses.append(myExpenses.pop())
        
        return render(request, 'expense_manager/recent_expenses.html', {'recentExpenses' : recentExpenses})
    
    total_expense = 0
    for expense in myExpenses:
        total_expense += expense.cost
    return render(request, 'expense_manager/expenses.html',{'expenses': myExpenses, 'total_expense' : total_expense})
    username = request.user.username