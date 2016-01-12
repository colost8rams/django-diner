from django.test import TestCase
from .models import Recipe, Ingredient, Instruction


class RecipeTestCase(TestCase):
    
    def setUp(self):
        Recipe.objects.create(title='Test recipe')
        
    
    def test_add_delete_ingredient(self):
        """
        Test the ability to create a new ingredient and add it to a recipe. Once
        added, then delete the ingredient.
        """
        r = Recipe.objects.get(title='Test recipe')
        i = r.ingredient_set.create(name='Ingredient 1')
        self.assertEqual(i.name, 'Ingredient 1')
        self.assertEqual(r.ingredient_set.count(), 1)
        i.delete()
        self.assertEqual(r.ingredient_set.count(), 0)
        
    
    def test_add_instruction(self):
        """
        Test the ability to create a new instruction and add it to a recipe. Once
        added, then delete the instruction.
        """
        r = Recipe.objects.get(title='Test recipe')
        i = Instruction.objects.create(recipe=r,description='Instruction 1')
        self.assertEqual(i.description, 'Instruction 1')
        self.assertEqual(r.instruction_set.count(), 1)
        i.delete()
        self.assertEqual(r.instruction_set.count(), 0)
    