from django.contrib import admin
from django.urls import path
from .views import RecipeListView, RecipeView


urlpatterns = [
    path("", RecipeListView.as_view(), name="recipes"),
    path("recipe/<int:pk>/",
        RecipeView.as_view(),
        name="recipe"),
]
