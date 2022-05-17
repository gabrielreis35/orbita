from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=500, verbose_name='Nome', unique=True)# Nome completo da disciplina
    minimum_time_completion = models.IntegerField(default=12)# Tempo minimo para conclusao do curso, em meses

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name
    
class Discipline(models.Model):
    name = models.CharField(max_length=500, verbose_name='Nome', unique=True)# Nome completo da disciplina

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name