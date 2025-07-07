from django import forms
from .models import Character, Weapon

class CharacterForm(forms.ModelForm):
    class Meta:
        model = Character
        fields = [
            'name', 'age', 'breed', 'class_name', 'inventory', 'equipment',
            'backstory', 'appearance', 'personality', 'alignment',
            'level', 'experience', 'hp', 'mp', 'strength', 'intelligence',
            'agility', 'luck', 'skills', 'weapon', 'character_image', 'privacy'
        ]
        widgets = {
            'character_image': forms.ClearableFileInput(attrs={'multiple': False}),
            'inventory': forms.Textarea(attrs={'rows': 3}),
            'equipment': forms.Textarea(attrs={'rows': 3}),
            'backstory': forms.Textarea(attrs={'rows': 3}),
            'appearance': forms.Textarea(attrs={'rows': 3}),
            'personality': forms.Textarea(attrs={'rows': 3}),
            'skills': forms.Textarea(attrs={'rows': 3}),
        }
        labels = {
            'character_image': 'Character Image',
            'name': 'Character Name',
            'age': 'Age',
            'breed': 'Breed',
            'class_name': 'Class',
            'inventory': 'Inventory',
            'equipment': 'Equipment',
            'backstory': 'Backstory',
            'appearance': 'Appearance',
            'personality': 'Personality',
            'alignment': 'Alignment',
            'level': 'Level',
            'experience': 'Experience',
            'hp': 'Health Points',
            'mp': 'Magic Points',
            'strength': 'Strength',
            'intelligence': 'Intelligence',
            'agility': 'Agility',
            'luck': 'Luck',
            'skills': 'Skills',
            'weapon': 'Weapon',
            'privacy': 'Privacy',
        }
        help_texts = {
            'character_image': 'Upload an image of your character.',
            'name': 'Enter the name of your character.',
            'age': 'Enter the age of your character.',
            'breed': 'Enter the breed of your character.',
            'class_name': 'Enter the class of your character.',
            'inventory': 'List items in your inventory.',
            'equipment': 'List equipped items.',
            'backstory': 'Write a backstory for your character.',
            'appearance': 'Describe your character\'s appearance.',
            'personality': 'Describe your character\'s personality.',
            'alignment': 'Enter the alignment of your character.',
            'level': 'Enter the level of your character.',
            'experience': 'Enter the experience points of your character.',
            'hp': 'Enter the health points of your character.',
            'mp': 'Enter the magic points of your character.',
            'strength': 'Enter the strength attribute of your character.',
            'intelligence': 'Enter the intelligence attribute of your character.',
            'agility': 'Enter the agility attribute of your character.',
            'luck': 'Enter the luck attribute of your character.',
            'skills': 'List skills of your character.',
            'privacy': 'Choose whether this character is public or private.',

        }
        error_messages = {
            'character_image': {
                'invalid': "Upload a valid image. The file you uploaded was either not an image or a corrupted image.",
            },
            'name': {
                'max_length': "This character's name is too long.",
            },
            'age': {
                'invalid': "Enter a valid age.",
            },
            'strength': {
                'invalid': "Enter a valid strength value.",
            },
            'intelligence': {
                'invalid': "Enter a valid intelligence value.",
            },
            'agility': {
                'invalid': "Enter a valid agility value.",
            },
            'luck': {
                'invalid': "Enter a valid luck value.",
            },
            'privacy': {
                'invalid_choice': 'Select a valid privacy option.',
            },
        }
class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = [
            'name', 'strength_needed', 'intelligence_needed', 'damage', 'description', 'weapon_image', 'weapon_type'
        ]
        widgets = {
            'description': forms.Textarea(attrs={'rows': 3}),
            'weapon_image': forms.ClearableFileInput(attrs={'multiple': False}),

        }
        labels = {
            'name': 'Weapon Name',
            'strength_needed': 'Strength Needed',
            'intelligence_needed': 'Intelligence Needed',
            'damage': 'Damage',
            'description': 'Description',
            'weapon_image': 'Weapon Image',
            'weapon_type': 'Weapon Type',
        }
        help_texts = {
            'name': 'Enter the name of the weapon.',
            'strength_needed': 'Enter the strength required to wield this weapon.',
            'intelligence_needed': 'Enter the intelligence required to wield this weapon.',
            'damage': 'Enter the damage dealt by this weapon.',
            'description': 'Describe the weapon.',
            'weapon_image': 'Upload an image of the weapon.',
            'weapon_type': 'Select the type of weapon.',
        }
        error_messages = {
            'name': {
                'max_length': "This weapon's name is too long.",
            },
            'strength_needed': {
                'invalid': "Enter a valid strength value.",
            },
            'intelligence_needed': {
                'invalid': "Enter a valid intelligence value.",
            },
            'damage': {
                'invalid': "Enter a valid damage value.",
            },
            'weapon_image': {
                'invalid': "Upload a valid image. The file you uploaded was either not an image or a corrupted image.",
            },
            'weapon_type': {
                'invalid_choice': "Select a valid choice. %(value)s is not one of the available choices.",
            },
        }
