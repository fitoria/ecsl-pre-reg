from django.db import models
from django.contrib.auth.models import User

PAISES = (
        ('Nicaragua', 'Nicaragua'),
        ('Costa Rica', 'Costa Rica'),
        ('Honduras', 'Honduras'),
        ('El Salvador', 'El Salvador'),
        ('Panama', 'Panama'),
        ('Guatemala', 'Guatemala'),
        ('Belice', 'Belice'),
        ('Mexico', 'Mexico'),
        ('Cuba', 'Cuba'),
        ('Venezuela', 'Venezuela'),
        ('Bolivia', 'Bolivia'),
        ('Colombia', 'Colombia'),
        ('Ecuador', 'Ecuador'),
        ('Paraguay', 'Paraguay'),
        ('Peru', 'Peru'),
        ('Puerto Rico', 'Puerto Rico'),
        ('Argentina', 'Argentina'),
        ('Uruguay', 'Uruguay'),
        ('Republica Dominicana', 'Republica Dominicana'),
        ('Haiti', 'Haiti'),
        ('Canada', 'Canada'),
        ('Estados Unidos', 'Estados Unidos'),
        ('Otros', 'Otros'),
        )

COMUNIDADES = (
        ('GUL-NIC', 'GUL-NIC'),
        ('Ubuntu-ni', 'Ubuntu-ni'),
        ('Fedora-ni', 'Fedora-ni'),
        ('Suse-ni', 'Suse-ni'),
        ('Debian-ni', 'Debian-ni'),
        ('Joomla-ni', 'Joomla-ni'),
        ('Asterik-ni', 'Asterik-ni'),
        ('Linux Users Group Belice','Linux Users Group Belice'),
        ('Ubuntu-cr', 'Ubuntu-cr'),
        ('Debian-cr', 'Debian-cr'),
        ('Red Costarricense de SL', 'Red Costarricense de SL'),
        ('Grupo de usuarios Linux Costa Rica', 'Grupo de usuarios Linux Costa Rica'),
        ('GUUG', 'GUUG'),
        ('Lugusag', 'Lugusac'),
        ('Shekalug', 'Shekalug'),
        ('Xelalug', 'Xelalug'),
        ('Guatejug', 'Guatejug'),
        ('GULTGU', 'GULTGU'),
        ('LUGSPS', 'LUGSPS'),
        ('GULPMA', 'GULPMA'),
        ('Ubuntu-pa', 'Ubuntu-pa'),
        ('Panama JUG', 'Panama JUG'),
        ('Geek Fest Panama', 'Geek Fest Panama'),
        ('Debian-pa', 'Debian-pa'),
        ('GNU-PA', 'GNU-PA'),
        ('Nodo Linux', 'Nodo Linux'),
        ('Open Source Revolution Panama', 'Open Source Revolution Panama'),
        ('GNU-SAL', 'GNU-SAL'),
        ('Ubuntu-sv', 'Ubuntu-sv'),
        ('LinUES', 'LinUES'),
        ('OpenSuseSv', 'OpenSuseSv'),
        ('Debian-sv', 'Debian-sv'),
        ('Linux-sv', 'Linux-sv'),
        ('Otro', 'Otro'),
        )

class UserProfile(models.Model):
    user = models.ForeignKey(User, verbose_name = 'Usuario')
    edad = models.PositiveIntegerField()
    telefono = models.CharField(max_length = 15, help_text = 'Favor introducir codigo de area', blank = True)
    pais = models.CharField(max_length = 100, choices = PAISES)
    gul = models.CharField(max_length = 200, choices = COMUNIDADES)
    website = models.URLField(blank = True)
    avatar = models.ImageField(upload_to = 'profiles/avatar', blank = True)
    comentario = models.TextField('Como se entero del encuentro?', blank = True)
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

    def get_absolute_url(self):
       return '/perfiles/%s' % self.user.username

    class Meta:
        verbose_name = "perfil"
        verbose_name = "perfiles"


