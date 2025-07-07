from django.shortcuts import render
from MainApp.models import Character, Weapon
from MainApp.forms import CharacterForm, WeaponForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

 
# Create your views here.

def index_general(request):
    Characters = Character.objects.filter(privacy='public')
    context = {
            'Characters': Characters,
            'General': True,
    }
    return render(request, 'index.html', context)

@login_required
def created_characters(request):
    Characters = Character.objects.filter(user=request.user).order_by('-created_at')
    context = {
        'Characters': Characters,
        'General': False,
    }
    return render(request, 'index.html', context)

@login_required
def character_detail(request, character_id):
    character = Character.objects.get(id=character_id)
    context = {
        'character': character,
    }
    return render(request, 'character_selected.html', context)

@login_required
def character_create(request):
    if request.method == 'POST':
        form = CharacterForm(request.POST, request.FILES)
        if form.is_valid():
            character = form.save(commit=False)
            character.user = request.user  # Asocia al usuario
            character.save()
            return redirect('index')
    else:
        form = CharacterForm()
    return render(request, 'character_creator.html', {'form': form})

@login_required
def weapon_create(request):
    if request.method == 'POST':
        form = WeaponForm(request.POST, request.FILES)
        if form.is_valid():
            weapon = form.save(commit=False)
            weapon.user = request.user
            weapon.save()
            return redirect('index')
    else:
        form = WeaponForm()
    return render(request, 'weapon_creator.html', {'form': form})

def weapon_list(request):
    Weapons = Weapon.objects.filter(privacy='public')
    context = {
        'Weapons': Weapons,
        'General': True
    }
    return render(request, 'weapon_list.html', context)

@login_required
def weapon_user_list(request):
    Weapons = Weapon.objects.filter(user=request.user)
    context = {
        'Weapons': Weapons,
        'General': False
    }
    return render(request, 'weapon_list.html', context)

@login_required
def delete_character(request, character_id):
    character = get_object_or_404(Character, id=character_id, user=request.user)
    character.delete()
    return redirect('index')

@login_required
def delete_weapon(request, weapon_id):
    weapon = get_object_or_404(Weapon, id=weapon_id, user=request.user)
    weapon.delete()
    return redirect('weapon_list')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
