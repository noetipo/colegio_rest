from uuid import uuid4
from django.db import models
class Persona(models.Model):
    TIPO_PERSONA_CHOICES = (
        (u'1', u'Profesor'),
        (u'2', u'Estudiante'),
        (u'3', u'Director'),
    )
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nombre = models.CharField(max_length=100 )
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno= models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)
    tipo_persona = models.CharField(max_length=1, choices=TIPO_PERSONA_CHOICES,default=2)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"
        
    def __str__(self):
        
        return '%s (%s)' % (self.nombre, self.tipo_persona)

class Periodo(models.Model):
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    periodo = models.CharField(max_length=100 )
    
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)
    

    class Meta:
        verbose_name = "Periodo"
        verbose_name_plural = "Periodos"
        
    def __str__(self):
        return self.periodo


class Materia(models.Model):
    """docstring for Seccion"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    materia = models.CharField(max_length=100)
    descripcion=models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Seccion"
        verbose_name_plural = "Seccions"
        
    def __str__(self):
        return self.materia

class Grado(models.Model):
    """docstring for Grado"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    grado = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    materia = models.ManyToManyField(Materia)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Grado"
        verbose_name_plural = "Grados"
        
    def __str__(self):
        return self.grado

class Seccion(models.Model):
    """docstring for Seccion"""
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    seccion = models.CharField(max_length=100)
    grado = models.ForeignKey(Grado)
    periodo = models.ForeignKey(Periodo)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Seccion"
        verbose_name_plural = "Seccions"
    def __str__(self):
        
        return '%s (%s)(%s)' % (self.seccion, self.grado, self.periodo)




class Matricula(models.Model):
    """docstring for Matricula"""
    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    seccion = models.ForeignKey(Seccion)
    persona = models.ForeignKey(Persona)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    estado = models.BooleanField(default=True)
    class Meta:
        verbose_name = "Seccion"
        verbose_name_plural = "Seccions"
    def __str__(self):
        return self.seccion
    

        
        




# Create your models here.
