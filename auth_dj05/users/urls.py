
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),    # Регистрация
    path('profile/', views.ProfileView.as_view(), name='profile'),  # Профиль
]