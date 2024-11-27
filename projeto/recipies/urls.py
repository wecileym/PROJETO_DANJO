from django.urls import path
from recipies import views


urlpatterns = [
    path('', views.home),
    path('recipes/<int:id>/', views.recipe),

]
