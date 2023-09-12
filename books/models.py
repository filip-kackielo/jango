from django.db import models

from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    year_of_birth = models.IntegerField(null=True)


class Category(models.Model):
    category_name = models.CharField(max_length=50)


