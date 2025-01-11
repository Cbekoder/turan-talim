from django.db import models


class Language(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to='languages/', null=True, blank=True)
    flag = models.CharField(max_length=8)

    def __str__(self):
        return self.name