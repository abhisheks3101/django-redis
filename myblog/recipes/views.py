from django.shortcuts import render
from django.views.generic import ListView, View
from .models import *
from django.http.response import HttpResponse
from django.core.cache import cache


class RecipeListView(ListView):
    queryset = Recipe.objects.all()
    context_object_name = 'recipes'
    template_name = "recipes/recipes.html"


class RecipeView(View):
    template_name = "recipes/recipe.html"
    def get(self, request, pk):
        recipe_id = pk

        if cache.get(recipe_id):
            recipe = cache.get(recipe_id)
            print("hit the cache")
        else:
            try:
                recipe = Recipe.objects.get(pk=recipe_id)
                cache.set(recipe_id, recipe)
                print("missed the cache")
            except Recipe.DoesNotExist:
                return HttpResponse('This is the reciepe template')
        
        context = {
            'recipe': recipe
        }
        return render(request, self.template_name, context)