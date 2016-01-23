from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import RecipeForm, IngredientFormSet, InstructionFormSet
from .models import Recipe



class RecipeListView(ListView):
    """
    Simple Django generic view that handles the list of recipes. In our case,
    the home page handles this with pagination.
    """
    model = Recipe
    template_name = "index.html"
    paginate_by = 5


class RecipeDetailView(DetailView):
    """
    Simple Django generic view that handles the detail page.
    """
    model = Recipe


class RecipeCreateView(CreateView):
    """
    Django generic CreateView with overrides to handle the ingredient and
    instruction inline formsets.
    """
    template_name = "recipe/recipe_form_create.html"
    model = Recipe
    form_class = RecipeForm
    
    def get_success_url(self):
        return self.object.get_absolute_url()
        
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        ingredient_form = IngredientFormSet()
        instruction_form = InstructionFormSet()
        
        return self.render_to_response(self.get_context_data(form=form,
            ingredient_form=ingredient_form,
            instruction_form=instruction_form))
    
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        ingredient_form = IngredientFormSet(self.request.POST)
        instruction_form = InstructionFormSet(self.request.POST)
        
        if (form.is_valid() and ingredient_form.is_valid() and
            instruction_form.is_valid()):
            return self.form_valid(form, ingredient_form, instruction_form)
        return self.form_invalid(form, ingredient_form, instruction_form)
    
    def form_valid(self, form, ingredient_form, instruction_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        
        ingredient_form.instance = self.object
        ingredient_form.save()
        
        instruction_form.instance = self.object
        instruction_form.save()
        
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form, ingredient_form, instruction_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(self.get_context_data(form=form,
            ingredient_form=ingredient_form,
            instruction_form=instruction_form))


class RecipeUpdateView(UpdateView):
    """
    Django generic UpdateView with overrides to handle the ingredient and
    instruction inline formsets.
    """
    template_name = "recipe/recipe_form_update.html"
    model = Recipe
    form_class = RecipeForm
    
    def get_success_url(self):
        return self.object.get_absolute_url()
        
    def get(self, request, *args, **kwargs):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        ingredient_form = IngredientFormSet(instance=self.object, prefix='ingredient')
        instruction_form = InstructionFormSet(instance=self.object, prefix='instruction')
        
        return self.render_to_response(self.get_context_data(form=form,
            ingredient_form=ingredient_form,
            instruction_form=instruction_form))
    
    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance and its inline
        formsets with the passed POST variables and then checking them for
        validity.
        """
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        
        ingredient_form = IngredientFormSet(self.request.POST, instance=self.object, prefix='ingredient')
        instruction_form = InstructionFormSet(self.request.POST, instance=self.object, prefix='instruction')
        
        if (form.is_valid() and ingredient_form.is_valid() and 
            instruction_form.is_valid()):
            return self.form_valid(form, ingredient_form, instruction_form)
        return self.form_invalid(form, ingredient_form, instruction_form)
    
    def form_valid(self, form, ingredient_form, instruction_form):
        """
        Called if all forms are valid. Creates a Recipe instance along with
        associated Ingredients and Instructions and then redirects to a
        success page.
        """
        self.object = form.save()
        ingredient_form.instance = self.object
        ingredient_form.save()
        instruction_form.instance = self.object
        instruction_form.save()
        return HttpResponseRedirect(self.get_success_url())
    
    def form_invalid(self, form, ingredient_form, instruction_form):
        """
        Called if a form is invalid. Re-renders the context data with the
        data-filled forms and errors.
        """
        return self.render_to_response(self.get_context_data(form=form,
            ingredient_form=ingredient_form,
            instruction_form=instruction_form))


class RecipeDeleteView(DeleteView):
    """
    Django generic DeleteView to handle the deletion of recipes.
    """
    model = Recipe
    success_url = reverse_lazy('recipe-list')