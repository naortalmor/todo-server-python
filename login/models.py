from django.db import models


# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mail = models.EmailField()
    image_url = models.URLField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
