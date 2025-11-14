
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


def register(request):
    """Обработка регистрации новых пользователей"""
    if request.method == 'POST':
        # Создаем форму с данными из запроса
        form = UserCreationForm(request.POST)

        # Проверяем валидность формы
        if form.is_valid():
            form.save()  # Сохраняем пользователя в базу данных

            # Показываем сообщение об успехе
            messages.success(request, 'Регистрация успешна! Теперь войдите в систему.')

            # Перенаправляем на страницу входа
            return redirect('login')
    else:
        # Если метод GET - показываем пустую форму
        form = UserCreationForm()

    # Рендерим шаблон с формой
    return render(request, 'registration/register.html', {'form': form})


class ProfileView(LoginRequiredMixin, TemplateView):
    """Страница профиля (только для авторизованных пользователей)"""
    template_name = 'registration/profile.html'
    login_url = '/login/'  # Куда перенаправить неавторизованных пользователей





