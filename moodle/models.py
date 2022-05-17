from django.db import models

class User(models.Model):
    TEACHER = 'TEACHER'
    STUDENT = 'STUDENT'
    COURSE_COORDNATOR = 'COURSE_COORDNATOR'
    POLO_COORDNATOR = 'POLO_COORDNATOR'
    ADMIN = 'ADMIN'
    MANAGER = 'MANAGER'
    TEST = 'TEST'
    WEBSERVER = 'WEBSERVER'
    TUTOR = 'TUTOR'
    ROLE_USER = (
        (TEACHER, 'Professor'),
        (STUDENT, 'Estudante'),
        (COURSE_COORDNATOR, 'Coordenador de Curso'),
        (POLO_COORDNATOR, 'Coordenador de Polo'),
        (MANAGER, 'Gerente'),
        (TUTOR, 'Tutor'),
        (ADMIN, 'Admin'),
        (TEST, 'Teste'),
        (WEBSERVER, 'Webserver'),
    )

    user_moodle_id = models.IntegerField(unique=True, verbose_name='ID Moodle')
    username = models.CharField(max_length=250, verbose_name='Nome de Usuario (Moodle)')# Nome completo
    fullname = models.CharField(max_length=250, verbose_name='Nome Completo')# Nome completo
    email = models.EmailField() # Email dele na plataforma
    role = models.CharField(max_length=20, 
                                   choices=ROLE_USER_MOODLE, default=STUDENT, verbose_name='Papel do Usuário (Moodle)')
    first_access = models.DateTimeField(verbose_name='Primeiro Acesso (Moodle)', blank=True, null=True)
    last_access = models.DateTimeField(verbose_name='Ultimo Acesso (Moodle)', blank=True, null=True)
    suspended = models.BooleanField(verbose_name='Suspenso (Moodle)', default=False)

    class Meta:
        ordering = ['fullname']

    def __str__(self):
        return str(self.fullname)