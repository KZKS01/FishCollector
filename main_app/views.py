from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def fishes_index(request):
    return render(request, 'fishes_index.html')

def fishes_detail(request):
    return render(request, 'fishes/detail.html')