from django.db import models

# Create your models here.

class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nomnre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

class Estudiante(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nomvres = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexo = [
        ('F', 'Femenino')
        ('M, Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='F')
    Carrera = models.ForeignKey(Carrera, null=false, blank=false, on_delete=models.CASCADE)
    vigencia = models.models.models.BooleanField(_(default=True))

    def nombrreCompleto(self):
        txt = "{0} {1} {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno), self.nombres

class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_Length=100)

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(_auto_now_add=True)