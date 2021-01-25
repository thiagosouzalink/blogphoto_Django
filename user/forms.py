from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class UserForm(forms.ModelForm):
    """ Formulário para cadastrar usuário"""

    username = forms.CharField(
        label='Usuário',
        error_messages= {
            'invalid': 'Nome de usuário inválido, informe apenas letras, números ou @, ., +, -, _',
            'max_length': 'Você excedeu o limite de caracteres.',
            'unique': 'Nome de usuário já existe.'
        },
        help_text= "Requeridos 150 caracteres ou menos. Letras, dígitos e @ /. / + / - / _ apenas",
        widget=forms.TextInput(attrs={'placeholder':'Username'})
    )

    email = forms.EmailField(
        label='E-mail',
        error_messages={'invalid': 'E-mail inválido.'},
        help_text='user@dominio.com',
        widget=forms.TextInput(attrs={'placeholder':'E-mail'})
    )

    first_name = forms.CharField(
        label='Nome',
        error_messages={'max_length': 'Nome não pode ter mais de 30 caracteres'},
        widget=forms.TextInput(attrs={'placeholder':'Nome'})
    )

    last_name = forms.CharField(
        label='Sobrenome',
        error_messages={'max_length': 'Sobrenome não pode ter mais de 150 caracteres'},
        widget=forms.TextInput(attrs={'placeholder':'Sobrenome'})
    )

    telefone = forms.CharField(
        label='Telefone',
        help_text='(xx) xxxxx-xxxx',
        widget=forms.TextInput(attrs={'placeholder':'Telefone...'})
    )
    password = forms.CharField(
        label='Senha',
        help_text="Digite uma senha segura",
        widget=forms.PasswordInput(attrs={'placeholder':'Senha'})
    )
    
    password2 = forms.CharField(
        label='Confirmar senha',
        widget=forms.PasswordInput(attrs={'placeholder':'Repetir senha'})
    )


    class Meta:
        model = CustomUser
        fields = (
            'username',
            'email',
            'first_name',   
            'last_name',
            'telefone'
        )

    def clean_password2(self):
        passwords = self.cleaned_data
        if passwords['password2'] != passwords['password']:
            raise forms.ValidationError("Senhas diferentes")

        return passwords['password2']

    def save(self, commit=True):
        user = CustomUser.objects.create_user(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            password=self.cleaned_data['password'],
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            telefone=self.cleaned_data['telefone']
        )
        return user


class UserProfileForm(forms.ModelForm):
    """ Formulário para atualizar dados do usuário"""

    facebook = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'https://www.facebook.com/seu_username'}), required=False)
    instagram = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'https://www.instagram.com/seu_username'}), required=False)
    twitter = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'https://www.twitter.com/seu_username'}), required=False)
    
    class Meta:
        model = CustomUser
        fields = fields = (
            'username',
            'email',
            'first_name',
            'last_name',
            'telefone',
            'facebook',
            'instagram',
            'twitter',
            'bio'
        )
        

class CustomUserCreateForm(UserCreationForm):
    """ Formulário para criar usuário no painel administrativo"""
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'telefone')
        labels = {'username': 'Username/E-mail'}

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.username = self.cleaned_data["username"]
        if commit:
            user.save()
        return user


class CustomUserChangeForm(UserChangeForm):
    """ Atualizar usuário no painel administrativo"""
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'telefone')


