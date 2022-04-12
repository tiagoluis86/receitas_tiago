from django.contrib.auth.models import User
from django.db import models  

# Create your models here.

class Profile(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Nome')
    last_name = models.CharField(max_length=100, verbose_name='Sobrenome')
    about_me = models.TextField(blank=True, null=True, verbose_name='Sobre mim')
    birthday = models.DateTimeField(null=True, verbose_name='Aniversário')
    member_since = models.DateTimeField(auto_now=True, verbose_name='Member since')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'profile'

    def __str__(self):
        return self.name

    def get_birthday(self):
        return self.birthday.strftime('%d/%m/%Y %H:%M Hrs')

    def get_member_since(self):
        return self.member_since.strftime('%Y-%m-%dT%H:%M')

class Receita(models.Model):
   
    foto = models.ImageField(upload_to ='img/')
    titulo = models.CharField(max_length=100)
    modo_de_fazer = models.TextField(blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
            db_table = "receita"

    def __str__(self):
            return self.titulo

   