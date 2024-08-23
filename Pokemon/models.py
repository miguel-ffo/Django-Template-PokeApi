from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=255, blank=True)
    type = models.CharField(max_length=255)
    image = models.URLField()


    def __str__(self):
        return self.name
