from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView
from django.views.generic import CreateView, ListView, UpdateView
from django.contrib import messages
from django.contrib.auth import (
    authenticate,
    login,
    logout
)

from .forms import UserForm, UserProfileForm
from .models import CustomUser
from photo.models import Photo


# # Página Inicial
class IndexView(ListView):

    model = Photo
    template_name = 'user/index.html'
    context_object_name = 'photos'

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_queryset(self):
        self.object_list = Photo.objects.filter(photo_user=self.request.user)
        return self.object_list    
    

# Página de Login
class LoginView(TemplateView):
    
    template_name = "user/login.html"


# Página de formulário de cadastro
class UserFormCadastro(CreateView):

    template_name = "user/cadastro.html"
    form_class = UserForm

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("login")


# Página para atualizar dados do usuário
class UserProfileUpdateView(UpdateView):

    template_name = 'user/profile.html'
    form_class = UserProfileForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_object(self):
        user_id = self.kwargs.get('user_id')
        user = self.request.user
        return get_object_or_404(CustomUser, id=user_id, username=user)

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("index")


# Página personalizada para mostrar postagem do usuário ao público
def user_home_perfil(request, username):
    template_name = 'user/home_perfil.html'
    current_user = request.user.username

    if current_user == username:
        return redirect('index')
    else:
        wanted_user = get_object_or_404(CustomUser, username=username)
        return render(request, template_name, {'wanted_user': wanted_user})


def submit_login(request):
    if request.POST:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password = password
        )

        if user:    
            login(request, user)
            return redirect("index")
        else:
            messages.error(
                request,
                "Login/Senha inválido! Por favor tente novamente."
            )
            return redirect("login")


def error_404(request, exception):
    return render(request, '404.html')






    


        