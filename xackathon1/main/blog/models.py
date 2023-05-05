from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    img = models.ImageField(upload_to='')

    def __str__(self):
        return self.title
