from django.urls import path
from recipies import views


urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('recipes/<int:id>/', views.recipe, name="recipes-recipe"),
]
