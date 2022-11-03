from django import forms
from .models import Contacto

class ContactoForm(forms.ModelForm):

    #nombre = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    #correo = forms.EmailField(widget=forms.TextInput(attrs={"class":"form-control"}))
    #tipo_consulta = forms.IntegerField(widget=forms.TextInput(attrs={"class":""}))
    
    class Meta:
        model = Contacto
        #para listarlos uno por uno
        # #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]

        #Para incluir de una todo el modelo
        fields = '__all__'
