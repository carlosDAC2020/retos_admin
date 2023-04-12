from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, "retos_admin/retos.html",{
        "seccion":"Lista de Retos"
    })


def login_admin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None and user.is_superuser:
            login(request, user)
            return redirect('retos_admin:index')
        else:
            return render(request, 'retos_admin/login.html', {'mensaje': 'Credenciales Invalidas'})
    else:
        return render(request, 'retos_admin/login.html')
