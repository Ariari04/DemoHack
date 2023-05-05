from django.contrib.auth.models import User
from django.db import models

RATING_CHOICES = ((1, 1),
                  (2, 2),
                  (3, 3),
                  (4, 4),
                  (5, 5))

# IMPORTANCE_CHOICES = (('Федеративное', 'Федеративное'),
#                       ('Областное', 'Областное'),
#                       ('Городское', 'Городское'),
#                       ('Сельское', 'Сельское')
#                       )


class Review(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='')
    street = models.CharField(max_length=100, null=True)
    rating = models.PositiveSmallIntegerField(choices=RATING_CHOICES)
    description = models.TextField(null=True, blank=True)
    importance = models.BooleanField(default=False)

    def __str__(self):
        return self.title