from django.db import models

# Create your models here.

#SE CREA EL MODELO DE CARRERAS
class Carrera(models.Model):
    codigo = models.CharField(max_length=3, primary_key=True)
    nombre = models.CharField(max_length=50)
    duracion = models.PositiveSmallIntegerField(default=5)

    #Codigo para mostrar los nombres de las carreras en las vistas (servidor) 

    def __str__(self):
        txt = "{0} (Duración: {1} año(s))"
        return txt.format(self.nombre, self.duracion)

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


    #Codigo para mostrar los nombres de las carreras en las vistas (servidor) 

    def __str__(self):
        txt = "{0} / Carrera: {1} / {2}"
        if self.vigencia:
            estadoEstudiante="VIGENTE"
        else:
            estadoEstudiante="DE BAJA"
        return txt.format(self.nombreCompleto(), self.carrera, estadoEstudiante)
#AGREGAR EL MODELO DE CURSOS

class Curso(models.Model):
    codigo = models.CharField(max_length=6, primary_key=True)
    nombre = models.CharField(max_length=30)
    creditos = models.PositiveSmallIntegerField()
    docente = models.CharField(max_length=100)

    def __str__(self):
        txt = "{0} ({1} / Docente: {2})"
        return txt.format(self.nombre, self.codigo, self.docente)

#AGREGAR EL MODELO DE MATRICULAS

class Matricula(models.Model):
    id = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(Estudiante, null=False, blank=False, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, null=False, blank=False, on_delete=models.CASCADE)
    fechaMatricula = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        txt = "{0} Matriculad{1} en el curso {2} / Fecha: {3}"
        if self.estudiante.sexo=='F':
            letraSexo='a'
        else:
            letraSexo= 'o'
        fechaMat = self.fechaMatricula.strftime("%A %d/%m/%Y %H:%M:%S")
        return txt.format(self.estudiante.nombreCompleto(), letraSexo, self.curso, fechaMat)

#Comentario a partir de acá
opciones_consultas = [
    [0, 'consulta'],
    [1, 'reclamo'],
    [2, 'sugerencia'],
    [3, 'felicitaciones']
]

class Contacto(models.Model):
    nombre = models.CharField(max_length=50, primary_key=True)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consultas)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    def __str__(self):
        return self.nombre
