from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DeleteView, UpdateView

from .models import Photo
from .forms import PhotoForm


class PhotoFormCreateView(CreateView):
    """ Formulário para criar postagem"""

    template_name = 'photo/cadastro.html'
    form_class = PhotoForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        photo = form.save(commit=False)
        photo.photo_user = self.request.user
        photo.save()
        return super(). form_valid(form)

    def get_success_url(self):
        return reverse('index')


class PhotoUpdateView(UpdateView):
    """ Formulário para editar postagem"""

    template_name = "photo/atualizar.html"
    form_class = PhotoForm

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_object(self):
        photo_id = self.kwargs.get('photo_id')
        user = self.request.user
        return get_object_or_404(Photo, id=photo_id, photo_user=user)
        
    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


class PhotoDeleteView(DeleteView):
    """ Excluir postagem"""

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get_object(self):
        photo_id = self.kwargs.get('photo_id')
        user = self.request.user
        return get_object_or_404(Photo, id=photo_id, photo_user=user)

    def get_success_url(self):
        return reverse('index')







