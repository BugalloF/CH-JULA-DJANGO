# from audioop import reverse
from django.db import models
from django.urls import reverse
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=128)
    friends=models.ManyToManyField("self",blank=True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un autor.
        """
        return reverse('person-detail', args=[str(self.id)])

class Lessons(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='School')

    def __str__(self):
        return self.name

class School(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    lessonsTaken = models.ForeignKey(Lessons, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField(default=1)

    class Meta:
        ordering=["-quantity"]
    def __str__(self):
        return f'{self.person} has taken {self.quantity} {self.lessonsTaken} lessons'