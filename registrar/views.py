from django.shortcuts import render
from .forms import RegistradoForm
from .models import Persona
# Create your views here.


def inicio (request):
    titulo = "Bienvenidos"
    form = RegistradoForm(request.POST or None )

    context = {
        "titulo": titulo,
        "form": form,
    }

    if form.is_valid():
        instance = form.save(commit=False)
        nombres = form.cleaned_data.get("nombres")
        cedula = form.cleaned_data.get("cedula_de_identidad")
        form.save()

        context = {
            "titulo": "gracias  %s, ya se ha registrado" %(nombres)

        }
        if not nombres:
            context = {
                "titulo": "gracias  %s, ya se ha registrado" % (cedula)

            }


        # print (instance.nombres)
    # if request.user.is_autenticated():
    #     titulo = "Hola, %s!" %(request.user)


    return render(request, "inicio.html", context)


def contact(request):
    titulo = "Contacto"
    #form = ContactForm(request.POST or None)

    # if form.is_valid():
    #     form_email = form.cleaned_data.get("email")
    #     form_mensaje = form.cleaned_data.get("mensaje")
    #     form_nombre = form.cleaned_data.get("nombre")
    #     asunto = 'Form de Contacto'

    context = {
        "form": form,
        "titulo": titulo,

    }
    return render(request, "forms.html", context)

def login (request):
    titulo = "Pantalla de Login"
    #form = RegistradoForm(request.POST or None )

    context = {
        "titulo": titulo,
    }
    return render(request, "login.html", context)


