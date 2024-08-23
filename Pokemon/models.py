from django.db import models

class Pokemon(models.Model):
    name = models.CharField(max_length=100, unique=True)
    type = models.CharField(max_length=50)
    image = models.URLField(max_length=200)
    ability = models.CharField(max_length=100, default='Unknown')  # Set default value here
    
    def __str__(self):
        return self.name
