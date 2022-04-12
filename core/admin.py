from django.contrib import admin
from core.models import Profile, Receita 

# Register your models here.


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'birthday', 'about_me')
    list_filter = ('usuario', 'birthday')

admin.site.register(Profile, ProfileAdmin) 


class ReceitaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'modo_de_fazer')
   
admin.site.register(Receita, ReceitaAdmin)