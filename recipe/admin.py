from django.contrib import admin
from .models import *


class IngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe','name',)
admin.site.register(Ingredient, IngredientAdmin)


class InstructionAdmin(admin.ModelAdmin):
    list_display = ('recipe','description',)
admin.site.register(Instruction, InstructionAdmin)


class RecipeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title','date_created',)
admin.site.register(Recipe, RecipeAdmin)
