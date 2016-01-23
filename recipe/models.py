from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from sorl.thumbnail import ImageField


class Ingredient(models.Model):
    """
    A model that defines ingredients associated with a recipe.
    """
    recipe = models.ForeignKey('Recipe', verbose_name="recipe")
    name = models.CharField(_("ingredient"), max_length=140, blank=True, null=True)
    
    class Meta:
        ordering = ["pk"]
    
    def __str__(self):
        return self.name
        

class Instruction(models.Model):
    """
    A model that defines instructions for a recipe.
    """
    recipe = models.ForeignKey('Recipe', verbose_name="recipe")
    description = models.TextField(_("instruction"), blank=True, null=True)
    
    class Meta:
        ordering = ["pk"]
        
    def __str__(self):
        return self.description
        

class Recipe(models.Model):
    """
    A model that defines a recipe.
    """
    title = models.CharField(_("name"), max_length=140)
    slug = models.SlugField(_("slug"), unique=True, blank=True, null=True)
    image = ImageField(upload_to="recipe/%Y/%m/%d", blank=True, null=True)
    description = models.TextField(_("description"), blank=True, null=True)
    
    servings = models.PositiveSmallIntegerField(_("servings"), blank=True, null=True)
    prep_time = models.PositiveSmallIntegerField(_("prep time"), blank=True, null=True)
    cook_time = models.PositiveSmallIntegerField(_("cook time"), blank=True, null=True)
    passive_time = models.PositiveSmallIntegerField(_("passive time"), blank=True, null=True)
    
    date_created = models.DateTimeField(auto_now_add=True,db_index=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ["-date_created"]
    
    def __str__(self):
        return self.title
        
    def get_absolute_url(self):
        return reverse("recipe-detail", kwargs={"slug": self.slug,})
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)[:50]
        super(Recipe, self).save(*args, **kwargs)
        
        