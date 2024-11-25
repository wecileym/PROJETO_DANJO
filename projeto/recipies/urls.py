from django.urls import path
from recipies.views import home, contato, sobre


urlpatterns = [
    path('', home),
    path('contato/', contato),
    path('sobre/', sobre)
]
