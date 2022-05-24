from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView,View

from .models import *

from django.core.cache import cache

class RecipesView(ListView):
    queryset: Recipe.objects.all()
    context_object_name = 'recipes'
    template_name: "recipes/recipe_list.html"

    def get_queryset(self):
        return Recipe.objects.all()

class RecipeView(View):
    template_name: "recipes/recipe.html"

    def get(self, request, **kwargs):

        recipe_id = kwargs["pk"] 

        if cache.get(recipe_id):
            recipe = cache.get(recipe_id)
            print('hit the cache')
        else:
            try:
                recipe = Recipe.objects.get(pk=recipe_id)
                cache.set(recipe_id,recipe)
                print('hit the db')
            except Recipe.DoesNotExist:
                return HttpResponse('no such recipe exists')

        context = {
            "recipe" : recipe,
        }

        return render(request,'recipes/recipe.html',context)

