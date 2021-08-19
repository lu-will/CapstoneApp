from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .models import day, evening


# Homepage
def home(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'pages/index.html', context)

# Login


def login_user(request):

    if request.method == "GET":
        return render(request, 'pages/login.html')

    elif request.method == "POST":
        print('FORM', request.POST)
        form = request.POST
        username = form['username']
        password = form['password']

        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)

        return HttpResponseRedirect(reverse('pages:login'))

# Logout


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('pages:home'))


# Register new user
def register(request):
    if request.method == "GET":
        return render(request, 'pages/register.html')
    elif request.method == "POST":
        form = request.POST
        username = form['username']
        password = form['password']
        email = form['email']
        first_name = form['first_name']
        last_name = form['last_name']

        user = User.objects.create_user(
            username, email, password, first_name=first_name, last_name=last_name)

        login(request, user)

        return HttpResponseRedirect(reverse('pages:register'))


# Day Journal Entries


def dayview(request):

    dayposts = day.objects.all()
    context = {
        'dayposts': dayposts
    }

    return render(request, 'pages/day.html', context)

# Lists the day entries for the index page

# def listdayentries(request):
#     dayposts = day.objects.all()
#     context = {
#         'dayposts': dayposts
#     }
#     return render(request, 'pages/index.html', context)


# Saved day entries

def savedayview(request):

    if request.method == "GET":
        return render(request, 'pages/day.html')

    elif request.method == "POST":
        form = request.POST
        date = form['datetime']
        prompt_1 = form['prompt_1']
        prompt_2 = form['prompt_2']
        prompt_3 = form['prompt_3']
        print(form)

        dayposts = day()
        dayposts.date = date
        dayposts.prompt_1 = prompt_1
        dayposts.prompt_2 = prompt_2
        dayposts.prompt_3 = prompt_3
        dayposts.save()

        context = {
            'dayposts': dayposts
        }
        return render(request, 'pages/index.html', context)


# Evening Journal Entries
def eveningview(request):
    eveningposts = evening.objects.all()

    context = {
        'eveningposts': eveningposts
    }
    return render(request, 'pages/evening.html', context)


# Saved evening entries
def saveeveningview(request):

    if request.method == "GET":
        return render(request, 'pages/evening.html')

    elif request.method == "POST":
        form = request.POST
        date = form['datetime']
        prompt_1 = form['prompt_1']
        prompt_2 = form['prompt_2']
        prompt_3 = form['prompt_3']
        print(form)

        eveningposts = evening()
        eveningposts.date = date
        eveningposts.prompt_1 = prompt_1
        eveningposts.prompt_2 = prompt_2
        eveningposts.prompt_3 = prompt_3
        eveningposts.save()

        context = {
            'eveningposts': eveningposts
        }
        return render(request, 'pages/index.html', context)


# User authentication

def userposts(request, username):
    user = get_object_or_404(User, username=username)
    context = {
        'user': user
    }
    return render(request, 'pages/userposts.html', context)
