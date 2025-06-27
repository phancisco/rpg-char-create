"""
URL configuration for RpgCharacterCreator project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
import MainApp.views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MainApp.views.index, name='index'),
    path('characters/<int:character_id>/', MainApp.views.character_detail, name='character_detail'),
    path('character/create/', MainApp.views.character_create, name='character_create'),
    path('weapon/create/', MainApp.views.weapon_create, name='weapon_create'),
    path('weapons/', MainApp.views.weapon_list, name='weapon_list'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', MainApp.views.register_view, name='register'),
    path('character/delete/<int:character_id>/', MainApp.views.delete_character, name='delete_character'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
