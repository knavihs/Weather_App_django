from django.db import models

# Create your models here.
class City(models.Model):
    Name= models.CharField(max_length=20)

    def __str__(self):
        return  self.Name

    class Meta:
        verbose_name_plural = "Cities"


