from django.shortcuts import render, redirect
from .models import Fish
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def signup(request):
    error_message = '' # declare it here to be overwritten later 
    # POST req
    if request.method == 'POST':
        # create a user in memory using UserCreationForm to validate form
        form = UserCreationForm(request.POST)
        # check if form inputs are valid
        if form.is_valid():
        # if valid: save new users to db as 'user'
            user = form.save()
            # login the new user
            login(request,user)
            # redirect to the cats index pg
            return redirect('fishes_index')
        # else: generate err msg 'invalid input'
        else: 
            error_message = 'Invalid signup - please check the requirements and try again'

    # GET req
        # sends an empty form to sign up
    form = UserCreationForm()
    return render(request, 'registration/signup.html', {
        'form': form,
        'error': error_message
    })
    
    
@login_required
def fishes_index(request):
    fishes = Fish.objects.all()
    return render(request, 'fishes/fishes_index.html', {'fishes': fishes})

@login_required
def fish_detail(request, fish_id):
    fish = Fish.objects.get(id=fish_id)
    return render(request, 'fishes/fish_detail.html', {'fish':fish})