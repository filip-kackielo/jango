from django.db import models

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    year_of_birth = models.IntegerField(null=True)


    # dodaj poniższą metodę
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.category_name}'


