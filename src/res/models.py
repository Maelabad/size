from django.db import models


class user_tee_shirt(models.Model):
    taille = models.IntegerField()
    poids = models.IntegerField()
    genre = models.CharField(max_length=1)


class user_pantalon(models.Model):
    tourTaille = models.IntegerField()
    tourHanche = models.IntegerField()
    genre = models.CharField(max_length=1)

class user_chaussures(models.Model):
    taille_pied = models.FloatField()
    genre = models.CharField(max_length=1)



