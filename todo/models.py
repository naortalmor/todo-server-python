from django.db import models

# Create your models here.
class Todo(models.Model):
    header = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    is_done = models.BooleanField(default=False)
    creation_date = models.DateField(auto_now_add=True)
    due_date = models.DateField(auto_now_add=False)

    def __str__(self):
        return self.header