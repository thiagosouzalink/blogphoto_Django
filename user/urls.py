from django.urls import path, include

from . import views


urlpatterns = [
    path('cadastro/', views.UserFormCadastro.as_view(), name='cadastro'),
    path('profile/<str:username>/<int:user_id>/', views.UserProfileUpdateView.as_view(), name='user_profile'),
    path('<str:username>/', views.user_home_perfil, name='user_home_perfil'),
]