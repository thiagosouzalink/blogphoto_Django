from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    """ Base para customizar User"""
    
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError("O nome de usuário é obrigatório.")
        if not email:
            raise ValueError("O E-mail é obrigatório,")
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(username, email, password, **extra_fields) 



class CustomUser(AbstractUser):

    email = models.EmailField('E-mail', unique=True)
    first_name = models.CharField('Nome', max_length=30)
    last_name = models.CharField('Sobrenome', max_length=150)
    telefone = models.CharField('Telefone', max_length=15)  
    is_staff = models.BooleanField('Membro da equipe', default=False)
    bio = models.TextField('Biografia', max_length=200, blank=True, help_text="Escreva no máximo 200 caracteres.")
    facebook = models.CharField('Facebook', max_length=100, blank=True)
    instagram = models.CharField('Instagram', max_length=100, blank=True)
    twitter = models.CharField('Twitter', max_length=100, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'telefone']

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'    

    def __str__(self):
        return self.username

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_profile_url(self):
        return reverse('user_profile', kwargs={'username': self.username, 'user_id': self.id})

    objects = UserManager()







