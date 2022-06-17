from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import Persona

# Create your views here.
def home(request):
    
    return render(request, "AppCoder/home.html")

def persona(self):
    p1 = Persona(nombre = "Sofia", apellido = "Gonella", dni = 1234, parentezco = "Hija", fechaNac = "1998-10-21")
    p1.save()

    p2 = Persona(nombre = "Karin", apellido = "Endendyk", dni = 22098, parentezco = "Madre", fechaNac = "1971-03-02")                              
    p2.save()

    p3 = Persona(nombre = "Angel", apellido = "Gonella", dni = 18433, parentezco = "Padre", fechaNac = "1967-11-01")
    p3.save()

    a = f"Mi nombre es: {p1.nombre}, Apellido: {p1.apellido}, dni: {p1.dni}, Parentezco: {p1.parentezco}, fecha de nacimiento: {p1.fechaNac}" 
    b = f"<br> Mi mama es: {p2.nombre}, Apellido: {p2.apellido}, dni: {p2.dni}, Parentezco: {p2.parentezco}, fecha de nacimiento: {p1.fechaNac}"
    c = f"<br> Mi papa es: {p3.nombre}, Apellido: {p3.apellido}, dni: {p3.dni}, Parentezco: {p3.parentezco}, fecha de nacimiento: {p1.fechaNac}"
    fam = a + b + c
    return HttpResponse(fam)