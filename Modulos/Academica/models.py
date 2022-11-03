from django.db import models

# Create your models here.

#SE CREA EL MODELO DE CARRERAS
class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

#AGREGAR EL MODELO DE ESTUDIANTES Y DEMÁS MODELOS
class Estudiante(models.Model):
    dni = models.CharField(max_length=8,primary_key=True)
    apellidoPaterno = models.CharField(max_length=35)
    apellidoMaterno = models.CharField(max_length=35)
    nombres = models.CharField(max_length=35)
    fechaNacimiento = models.DateField()
    sexos = [
        ('F', 'Femenino'),
        ('M', 'Masculino')
    ]
    sexo = models.CharField(max_length=1, choices=sexos, default='M')
    carrera = models.ForeignKey(Carrera, null=False, blank=False, on_delete=models.CASCADE)
    vigencia = models.BooleanField(default=True)

    def nombreCompleto(self):
        txt = "{0} {1}, {2}"
        return txt.format(self.apellidoPaterno, self.apellidoMaterno, self.nombres)

#AGREGAR EL MODELO DE CURSOS

class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)

#AGREGAR EL MODELO DE MATRICULAS

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)
