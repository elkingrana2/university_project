from django.shortcuts import render
from django.conf import settings 
from django.core.mail import send_mail
from .forms import ContactoForm

# Create your views here.

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto Guardado"
        else:
            data["form"] = formulario
    return render(request, 'contacto.html', data)

#Crear una primera vista llamada formularioContacto
#Render es una función que permite indicar la respuesta que se va a optener a partir de una petición
#def formularioContacto(request):
 #   return render(request, "formularioContacto.html")

#def contactar(request):
 #   if request.method == "POST":
  #      asunto = request.POST["txtAsunto"]
   #     mensaje = request.POST["txtMensaje"] + " / Email: " + request.POST["txtEmail"] 
    #    email_desde = settings.EMAIL_HOST_USER
     #   email_para = ["elkingc1@gmail.com"]
      #  send_mail(asunto, mensaje, email_desde, email_para, fail_silenty=False)
       # return render(request, "contactoExitoso.html")
    #return render(request, "formularioContacto.html")