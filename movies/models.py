from django.db import models

# Create your models here.
class Movie(models.Model):
    tytle = models.CharField(max_length=30, null=False)
    MOVIES_GENDER={
        ('A','Animación'),
        ('c','Comedia'),
        ('F','Familiar'),
        ('H','Heroes'),
        ('S','Suspenso'),
        ('T','Terror'),
    }
    
    
    gender = models.CharField(max_length=30, choices=MOVIES_GENDER, null=False)
    director = models.CharField(max_length=30, null=False)
    year = models.BigIntegerField(null=False)
    synopsis = models.CharField(max_length=100, null=False)
    
    def __str__(self) -> str:
        return self.tytle
    
    
    