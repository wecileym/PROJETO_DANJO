from django.shortcuts import render
from django.http import HttpResponse
from utils.recipes.factory import make_recipe
from recipies.models import Recipe
from django.http import Http404
from django.shortcuts import get_list_or_404, render



# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'recipies/pages/home.html', context={
        'recipes': recipes,
    })

def category(request, category_id):
      recipes = get_list_or_404(
        Recipe.objects.filter(
            category__id=category_id,
            is_published=True,
        ).order_by('-id')
    )

      return render(request, 'recipies/pages/category.html', context={
            'recipes': recipes,
            'title': f'{recipes[0].category.name} - Category | '
        })


def recipe(request, id):

    recipe=Recipe.objects.filter(
            pk=id,
            is_published=True,
        ).order_by('-id').first()
    
    return render(request, 'recipies/pages/category.html', context={
      
      'recipe': recipe,
      'is_datail_page': True,
 
    })