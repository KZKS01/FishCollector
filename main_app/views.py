from django.shortcuts import render, redirect
from .models import Fish, Tank, Photo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import boto3 #aws
import uuid

S3_BASE_URL = 'https://s3.us-east-2.amazonaws.com/'
BUCKET = 'fishcollector'


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
            # redirect to the fishes index pg
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
    
# FISH 
@login_required
def fishes_index(request):
    fishes = Fish.objects.filter(user=request.user)
    return render(request, 'fishes/fishes_index.html', {'fishes': fishes})

@login_required
def fish_detail(request, fish_id):
    fish = Fish.objects.get(id=fish_id)
    return render(request, 'fishes/fish_detail.html', {'fish':fish})

class FishAdd(LoginRequiredMixin, CreateView):
    model = Fish
    fields = ('name', 'species', 'age','description') # specifics which fields we r providing data for
    template_name = 'fishes/fish_form.html'

    # take validated inputs to create a model instance
    def form_valid(self,form): # self: the instance of the view that is handling the form submission. form parameter contains the validated form data.
        # form.instance attr: the instance of the model that is being created or updated by the form
        # overwrite its method before the form is created
        form.instance.user = self.request.user # self.request.user: user that made the request to the view
        # tells Django to execute the form_valid() method defined in the parent CreateView class
        # & let it handle the task of creating the new Fish instance in the db
        # The super() function allows us to reuse the code written in the parent class, and only add the specific functionality we want in the child class.
        return super().form_valid(form)
 
class FishUpdate(LoginRequiredMixin, UpdateView):
    model = Fish
    fields = ('name', 'species', 'age', 'description')
    template_name = 'fishes/fish_form.html'

class FishDelete(LoginRequiredMixin, DeleteView):
    model = Fish
    template_name = 'fishes/fish_confirm_delete.html'
    success_url = '/fishes/'


# TANK
def tanks_index(request):
    tanks = Tank.objects.all()
    return render(request, 'tanks/tanks_index.html', {'tanks':tanks})

class TankAdd(LoginRequiredMixin, CreateView):
    model = Tank
    fields = ('size',)
    template_name = 'tanks/tank_form.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class TankUpdate(LoginRequiredMixin, UpdateView):
    model = Tank
    fields = ('size', )
    template_name = 'tanks/tank_form.html'

class TankDelete(LoginRequiredMixin, DeleteView):
    model = Tank
    template_name = 'tanks/tank_confirm_delete.html'
    success_url = '/tanks/'


# PHOTO
def add_photo(request, fish_id):
    # attempt to collect photo submission from request
    photo_file = request.FILES.get('photo-file', None)# FILES: dictionary
    # if photo file is present
    if photo_file:
        # set up a s3 client obj - obj w/methods for working with s3
        s3 = boto3.client('s3')
        # create a UNIQUE name for the photo file with uuid
        key = uuid.uuid4().hex[:6] + photo_file.name[photo_file.name.rfind('.'):]
        
        # try to upload file to aws s3
        try:
            # upload file to the specified s3 bucket via method: s3.upload_fileobj()
            s3.upload_fileobj(photo_file, BUCKET, key) 
            # save the url as a new instance of the Photo model
            url = f'{S3_BASE_URL}{BUCKET}/{key}'
            # new instance of the Photo model created with the url and fish_id val, associating the photo with the given fish_id 
            Photo.objects.create(url=url, fish_id=fish_id)
        # if error
        except Exception as error:
            print('Photo upload failed, error: ', error)
        return redirect('fish_detail', fish_id=fish_id)