from django.db import models

# Create your models here.


class Contact(models.Model):
    name = models.CharField(max_length=100)
    message = models.TextField()
    phone = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
