import uuid
from django.db import models
from django.urls import reverse

from stdimage.models import StdImageField

from user.models import CustomUser


# Definir local e nome da foto
def get_file_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = f"user_{instance.photo_user.username}-id_{instance.photo_user.id}/{instance.photo_user.username}-{instance.photo_user.id}-{str(uuid.uuid4())}.{ext}"
    return filename

class Photo(models.Model):

    photo_user = models.ForeignKey(CustomUser, verbose_name='Usuário', on_delete=models.CASCADE)
    photo_url = StdImageField('Imagem', default='profile.png', upload_to=get_file_path, variations={'thumb': {'width':480, 'height':480, 'crop': True}}, null=True)
    description = models.TextField('Descrição', max_length=200, blank=True)
    created_at = models.DateField('Criado', auto_now_add=True)

    class Meta:
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

    def __str__(self):
        return f"{self.photo_user}-{self.photo_url}"

    def get_update_url(self):
        return reverse('photo_update', kwargs={'username': self.photo_user, 'photo_id': self.id})

    def get_delete_url(self):
        return reverse('photo_delete', kwargs={'username': self.photo_user,'photo_id': self.id})

    def get_home_perfil_url(self):
        return reverse('user_home_perfil', kwargs={'username': self.photo_user})