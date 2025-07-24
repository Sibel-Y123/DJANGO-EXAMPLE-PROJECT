from django.urls import path
from .views import user_login, register, welcome_view
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', welcome_view, name='welcome'),
    path('login/', user_login, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'), 
]
