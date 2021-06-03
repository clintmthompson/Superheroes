from django.db import models


class Superheroes(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_ability = models.CharField(max_length=50)
    secondary_ability = models.CharField(max_length=50)
    catch_phrase = models.CharField(max_length=50)

    def __str__(self):
        return self
