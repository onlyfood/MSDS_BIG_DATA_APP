from django.db import models

# Create your models here.


class Message(models.Model):
    content = models.TextField()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    publication_date = models.DateField()
    # Add other fields as needed

    def __str__(self):
        return self.title
