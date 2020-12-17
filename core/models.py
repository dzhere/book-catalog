from django.db import models
from django_countries.fields import CountryField

class Author(models.Model):
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    birtday_date = models.DateField(blank=True, null=True)
    country = CountryField(blank=True, null=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    genre = models.ForeignKey('Genre', on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    country = CountryField(blank=True, null=True)

    def __str__(self):
        return f'{self.authors}: {self.title}'
