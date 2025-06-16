from django.contrib import messages
from django.shortcuts import render, redirect
from .models import reserva

# Create your views here.

def home(request):
    return render(request, 'app/home.html') 


def agendar(request):
    if request.method == 'POST':
        nombre_dueño = request.POST.get('dueno')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')
        nombre_mascota = request.POST.get('animalname')
        raza = request.POST.get('breedname')
        fecha_reserva = request.POST.get('fecha')
        estado = request.POST.get('estado')
        motivo = request.POST.get('motivo')

        reserva.objects.create(
            nombre_dueño=nombre_dueño,
            correo=correo,
            direccion=direccion,
            nombre_mascota=nombre_mascota,
            raza=raza,
            fecha_reserva=fecha_reserva,
            estado=estado,
            motivo=motivo
        )

        messages.success(request, 'reserva ehcha con exito')
        return redirect ('home')
    return render(request, 'app/agendar.html')

def nav(request):
    return render(render, 'app/nav_foot/nav')