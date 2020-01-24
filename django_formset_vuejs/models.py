from django.contrib.auth.models import User
from django.db import models


class AuthorContainer(models.Model):
    created = models.DateField(auto_now=True, null=True)

    def __str__(self):
        return '{}'.format(self.created)


class Author(models.Model):
    author_container = models.ForeignKey(AuthorContainer, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, null=True, blank=True)
    isbn = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return '{}'.format(self.title)



