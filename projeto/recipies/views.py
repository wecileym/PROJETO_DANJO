from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'recipies/pages/home.html')

def recipe(request, id):
    return render(request, 'recipies/pages/recipe-view.html')