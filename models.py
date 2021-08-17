from django.db import models


SIZE_CHOICES = (
   ('А4', 'А4'),
   ('А3', 'А3')
)


TECHNIC_CHOICES = (
   ('R', 'Реалистичная'),
   ('H', 'Художественная')
)


class Post(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    link = models.CharField(max_length=100)
    size = models.CharField(choices=SIZE_CHOICES, max_length=128)
    technic = models.CharField(choices=TECHNIC_CHOICES, max_length=128)
    thoughts = models.TextField()
    photo = models.ImageField()

    def __str__(self):
        return self.name
