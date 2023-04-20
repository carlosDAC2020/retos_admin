from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login



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


# -------------- Retos ------------------------------------
def index(request):
    print("retos")
    return render(request, "retos_admin/retos/retos.html",{
        "retos":range(1,11)
    })

def create_retos(request):
    if request.method == 'POST':
        return redirect('retos_admin:retos_detail')
    else:
        return render(request, 'retos_admin/retos/create.html')

def retos_detail(request):
    return render(request, 'retos_admin/retos/detail.html')

    # ----------- comunidades -------------------------
def comunidades(request):
    print("comunidades")
    return render(request, 'retos_admin/comunidades/comunidades.html',{
        "comunidades":range(1,15)
    })

def create_comunidades(request):
    if request.method == 'POST':
        return redirect('retos_admin:comunidades_detail')
    else:
        return render(request, 'retos_admin/comunidades/create.html')

def comunidades_detail(request):
    return render(request, 'retos_admin/comiunidades/detail.html')

    # ----------- Instituciones -----------------------------------
def instituciones(request):
    print("instituciones")
    return render(request, "retos_admin/instituciones/instituciones.html",{
        "instituciones":range(1,11)
    })

def create_instituciones(request):
    if request.method == 'POST':
        return redirect('retos_admin:instituciones_detail')
    else:
        return render(request, 'retos_admin/instituciones/create.html')

def instituciones_detail(request):
    return render(request, 'retos_admin/instituciones/detail.html')

    # ----------- espacios de co creacion -------------------------
def esp_co_creacion(request):
    print("espacios de cocreacion")
    return render(request, "retos_admin/esp_co_creacion/esp_co_creacion.html",{
        "esp_co_creacion":range(1,11)
    })

def create_esp_co_creacion(request):
    if request.method == 'POST':
        return redirect('retos_admin:esp_co_creacion_detail')
    else:
        return render(request, 'retos_admin/esp_co_creacion/create.html')

def esp_co_creacion_detail(request):
    return render(request, 'retos_admin/esp_co_creacion/detail.html')

    # ----------- Participantes -------------------------------------
def participantes(request):
    print("participantes")
    return render(request, "retos_admin/participantes/participantes.html",{
        "participantes":range(1,11)
    })

def create_participantes(request):
    if request.method == 'POST':
        return redirect('retos_admin:participantes_detail')
    else:
        return render(request, 'retos_admin/participantes/create.html')

def participantes_detail(request):
    return render(request, 'retos_admin/participantes/detail.html')