from django.db import models
from django.contrib.auth.models import User

ITEM_TYPES = (("starter","Starter"),("main","Main"),("desert","Desert"),("drink","Drink"),("side", "Side"))


class MenuItem(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=25, choices=ITEM_TYPES, default='starter')
    description = models.TextField(default="")
    price = models.FloatField(default=0.00)
    contains_nuts = models.BooleanField(default=False)
    vegetarian = models.BooleanField(default=False)
    vegan = models.BooleanField(default=False)
    gluten_free = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['type', 'name']

    def __str__(self):
        return str(self.name)
    
class Menu(models.Model):
    name = models.CharField(max_length=25)
    active = models.BooleanField(default=False)
    starters = models.ManyToManyField('MenuItem', related_name='starters')
    mains = models.ManyToManyField('MenuItem', related_name='mains')
    deserts = models.ManyToManyField('MenuItem', related_name='deserts')
    drinks = models.ManyToManyField('MenuItem', related_name='drinks')
    sides = models.ManyToManyField('MenuItem', related_name='sides')
    
    
    
    class Meta:
        ordering = ['-active', 'name']

    def __str__(self):
        return str(self.name)