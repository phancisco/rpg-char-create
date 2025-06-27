from django.contrib import admin
from MainApp.models import Character, Weapon

# Register your models here.

class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'age', 'breed', 'class_name', 'inventory', 'equipment', 'backstory',
        'appearance', 'personality', 'alignment', 'level', 'experience', 'hp', 'mp',
        'strength', 'intelligence', 'agility', 'luck', 'skills', 'weapon',
        'created_at', 'updated_at'
    )

class WeaponAdmin(admin.ModelAdmin):
    list_display = (
        'name', 'damage', 'strength_needed', 'intelligence_needed', 'weapon_type',
        'description', 'weapon_image'
    )

admin.site.register(Character, CharacterAdmin)
admin.site.register(Weapon, WeaponAdmin)