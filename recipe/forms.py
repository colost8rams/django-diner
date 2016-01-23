from django import forms
from django.forms.models import inlineformset_factory

from .models import Recipe, Ingredient, Instruction


def add_bootstrap_classes(f, **kwargs):
    """
    Formfield callback that adds a CSS class to every field indicating
    what kind of field it is. For example, all CharField inputs will get
    a class of "vCharField". If the field's widget already has a
    "class" attribute, it will be left alone.

    Example:

    class MyForm(forms.ModelForm):
        formfield_callback = add_css_classes
    """
    field = f.formfield(**kwargs)
    if field and 'class' not in field.widget.attrs:
        field.widget.attrs['class'] = 'form-control input-sm'
    return field
    

class RecipeForm(forms.ModelForm):
    """
    Django ModelForm view that handles the recipe form. NOTE: We do use the
    formfield_callback to apply Bootstrap form classes to all fields.
    """
    formfield_callback = add_bootstrap_classes
    
    class Meta:
        model = Recipe
        fields = '__all__'
        exclude = ['slug']

        

class IngredientForm(forms.ModelForm):
    """
    Django ModelForm view that handles the ingredient form. NOTE: Due to the
    way Django handles formsets, we need to directly apply the the
    Bootstrap form classes to all fields.
    """
    
    class Meta:
        model = Ingredient
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(IngredientForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['class'] = 'form-control'
        

class InstructionForm(forms.ModelForm):
    """
    Django ModelForm view that handles the ingredient form. NOTE: Due to the
    way Django handles formsets, we need to directly apply the the
    Bootstrap form classes to all fields.
    """
    
    class Meta:
        model = Instruction
        fields = "__all__"
    
    def __init__(self, *args, **kwargs):
        super(InstructionForm, self).__init__(*args, **kwargs)
        self.fields['description'].widget.attrs['rows'] = '5'
        self.fields['description'].widget.attrs['class'] = 'form-control'
        
        
IngredientFormSet = inlineformset_factory(Recipe,Ingredient,
    form = IngredientForm,
    extra = 2,
    fields = "__all__",
    can_delete = True)

InstructionFormSet = inlineformset_factory(Recipe,Instruction,
    form = InstructionForm,
    extra = 2,
    fields = "__all__",
    can_delete = True)