from django.db import models

# Create your models here.
class Departamento(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField('Nombre',max_length=100,null=False)
    class Meta:
        verbose_name="Departamento"
        verbose_name_plural="Departamentos"
        ordering=['nombre']
    def __str__(self) :
        return self.nombre

class JefeDepartamento(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField('Nombres',max_length=100,null=False)
    apellido=models.CharField('Apellidos',max_length=100)
    dni=models.IntegerField("Dni",null=False)
    email=models.EmailField('Email',blank=False,null=True)
    id_departamento=models.OneToOneField(Departamento,on_delete=models.CASCADE)
    class Meta:
        verbose_name="Jefe de Departamento"
        verbose_name_plural="Jefes de Departamentos"
        ordering=['nombre']
    def __str__(self) :
        return self.nombre

class Carrera(models.Model):
    id=models.CharField(primary_key=True,max_length=4)
    nombre=models.CharField('Nombre',max_length=100,null=False)
    ciclo=models.IntegerField("Ciclos",null=False)
    id_departamento=models.ForeignKey(Departamento,on_delete=models.CASCADE)
    class Meta:
        verbose_name="Carrera"
        verbose_name_plural="Carreras"
        ordering=['nombre']
    def __str__(self) :
        return self.nombre

class Curso(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField('Nombre',max_length=100,null=False)
    horas=models.FloatField("Horas",max_length=5,null=False)
    creditos=models.IntegerField("Creditos",null=False)
    id_carrera=models.ForeignKey(Carrera,on_delete=models.CASCADE)
    class Meta:
        verbose_name="Curso"
        verbose_name_plural="Cursos"
        ordering=['nombre']
    def __str__(self) :
        return self.nombre

class Profesor(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField('Nombres',max_length=100,null=False)
    apellido=models.CharField('Apellidos',max_length=100)
    dni=models.IntegerField("Dni",null=False)
    email=models.EmailField('Email',blank=False,null=True)
    id_curso=models.ManyToManyField(Curso)

    class Meta:
        verbose_name="Profesor"
        verbose_name_plural="Profesores"
        ordering=['nombre']
    def __str__(self) :
        return self.nombre





class Alumno(models.Model):
    id=models.AutoField(primary_key=True)
    nombre=models.CharField('Nombres',max_length=100,null=False)
    apellido=models.CharField('Apellidos',max_length=100)
    dni=models.IntegerField("Dni",null=False) 
    email=models.EmailField('Email',blank=False,null=True)
    ciclo=models.IntegerField("Ciclo",null=False)
    id_curso=models.ManyToManyField(Curso)
    class Meta:
        verbose_name="Alumno"
        verbose_name_plural="Alumnos"
        ordering=['nombre']
    def __str__(self) :
        return self.nombre

class Aula(models.Model):
    id=models.IntegerField(primary_key=True)
    capacidad=models.IntegerField("Capacidad",null=False)
    id_curso=models.ManyToManyField(Curso)
    class Meta:
        verbose_name="Aula"
        verbose_name_plural="Aulas"
        ordering=['id']
    def __int__(self) :
        return self.id