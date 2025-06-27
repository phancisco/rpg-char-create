from django.db import models
from django.contrib.auth.models import User

# Create your models here.
WEAPON_TYPE_CHOICES = [
    ('magic', 'Magic'),
    ('melee', 'Melee'),
    ('ranged', 'Ranged'),
]
class Weapon(models.Model):
    weapon_image = models.ImageField(upload_to='weapons/', null=True, blank=True)
    weapon_type = models.CharField(max_length=10, choices=WEAPON_TYPE_CHOICES, default='melee')
    strength_needed = models.IntegerField()
    intelligence_needed = models.IntegerField()
    name = models.CharField(max_length=100)
    damage = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
class Character(models.Model):
    # Basic Information
    character_image = models.ImageField(upload_to='characters/', null=True, blank=True)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100)
    class_name = models.CharField(max_length=100)
    inventory = models.TextField()
    equipment = models.TextField()
    backstory = models.TextField()
    appearance = models.TextField()
    personality = models.TextField()
    alignment = models.CharField(max_length=100)

    # Combat Attributes
    level = models.IntegerField()
    experience = models.IntegerField()
    hp = models.IntegerField()
    mp = models.IntegerField()
    strength = models.IntegerField()
    intelligence = models.IntegerField()
    agility = models.IntegerField()
    luck = models.IntegerField()
    skills = models.TextField()
    weapon = models.ForeignKey(Weapon , on_delete=models.CASCADE, null=True, blank=True)


    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name