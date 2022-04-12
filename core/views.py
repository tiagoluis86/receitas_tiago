from xml.sax import default_parser_list
from django.shortcuts import render
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from datetime import datetime, timedelta
from django.http.response import Http404
from core.models import Profile, Receita

# Create your views here.




def loginpage(request):
    return render(request, "login.html")

def logout_user(request):
    logout(request)
    return redirect('/')    

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/')

@login_required(login_url="/login/")
def index(request):
    usuario = request.user
    profile = Profile.objects.filter(usuario=usuario)
    receita = Receita.objects.filter(usuario=usuario)
    info = {'receitas':receita, 'profiles':profile}   
    return render(request, "index.html", info)
   