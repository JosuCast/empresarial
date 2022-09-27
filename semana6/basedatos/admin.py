from django.contrib import admin

class DepartamentoAdmin(admin.ModelAdmin):
    list_display=("id","nombre")
    search_fields=("id","nombre")
    list_filter=("nombre",)

class ProfesorAdmin(admin.ModelAdmin):
    list_display=("id","nombre","apellido","dni","email",'cursos')
    def cursos(self,obj):
        return "\n, ".join([str(p.nombre) for p in obj.id_curso.all()])
    search_fields=("id","nombre","apellido","dni",'cursos')
    list_filter=("id_curso","apellido")

class JefeDepartamentoAdmin(admin.ModelAdmin):
    list_display=("id","nombre","apellido","dni","email","id_departamento")
    search_fields=("id","nombre","apellido","dni","id_departamento")
    list_filter=("apellido","id_departamento")
class CarreraAdmin(admin.ModelAdmin):
    list_display=("id","nombre","ciclo","id_departamento")
    search_fields=("id","nombre","ciclo","id_departamento")
    list_filter=("id","nombre","id_departamento")

class CursoAdmin(admin.ModelAdmin):
    list_display=("id","nombre","horas","creditos","id_carrera")
    search_fields=("id","nombre","horas","creditos","id_carrera")
    list_filter=("id","nombre","id_carrera")

class AlumnoAdmin(admin.ModelAdmin):
    list_display=("id","nombre","apellido","dni","email","cursos","ciclo")
    def cursos(self,obj):
        return "\n, ".join([str(p.nombre) for p in obj.id_curso.all()])
    search_fields=("id","nombre","apellido","dni","ciclo")
    list_filter=("id","nombre","apellido","id_curso","ciclo")

class AulaAdmin(admin.ModelAdmin):
    list_display=("id","capacidad","cursos")
    def cursos(self,obj):
        return "\n, ".join([str(p.nombre) for p in obj.id_curso.all()])
    search_fields=("id","capacidad","cursos")
    list_filter=("id_curso",)

# Register your models here.
from .models import Alumno, Aula, Carrera, Curso, Departamento, JefeDepartamento, Profesor

admin.site.register(Departamento,DepartamentoAdmin)
admin.site.register(Profesor,ProfesorAdmin)
admin.site.register(JefeDepartamento,JefeDepartamentoAdmin)
admin.site.register(Carrera,CarreraAdmin)
admin.site.register(Curso,CursoAdmin)
admin.site.register(Alumno,AlumnoAdmin)
admin.site.register(Aula,AulaAdmin)