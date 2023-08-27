from django.db import models
from applications.departamento.models import Departamento
from ckeditor.fields import RichTextField

# Create your models here.
class Habilidades(models.Model):
    habilidad = models.CharField('Habilidad', max_length=50)

    class Meta:
        verbose_name = 'Habilidades'
        verbose_name_plural = 'Habilidades'

    def __str__(self):
        return str(self.id) + '-' + self.habilidad

class Empleado(models.Model):

    job_choices = (
        ('0', 'Contador'), 
        ('1', 'Administrador'), 
        ('2', 'Economista'), 
        ('3', 'Otro')
    )

    first_name = models.CharField('Nombres', max_length=60)
    last_name = models.CharField('Apellidos', max_length=60)
    full_name = models.CharField('Nombres Completos', max_length=120, blank=True)
    job = models.CharField('Trabajo', max_length=1, choices=job_choices)
    departamento = models.ForeignKey(Departamento, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='empleado', blank=True, null=True)
    habilidades = models.ManyToManyField(Habilidades)
    hoja_vida = RichTextField()


    class Meta:
        ordering = ['-first_name', 'last_name']
        unique_together = ('first_name', 'departamento')

    def __str__(self):
        return str(self.id) + '-' + self.first_name + '-' + self.last_name