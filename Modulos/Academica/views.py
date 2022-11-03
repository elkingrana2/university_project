from django.shortcuts import render
# Create your views here.

#Crear una primera vista llamada formularioContacto
#Render es una función que permite indicar la respuesta que se va a optener a partir de una petición
def formularioContacto(request):
    return render(request, "formularioContacto.html")
