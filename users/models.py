from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import format_html
from django.utils.text import slugify
from autoslug import AutoSlugField

class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class City(models.Model):
    name = models.CharField(max_length=50)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Prefer not to say', 'Prefer not to say'),
)

class User(AbstractUser):
    phone = models.CharField(max_length=13, unique=True, blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pictures', blank=True, null=True)
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES, blank=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    balance = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username



class Teachers(models.Model):
    slug = AutoSlugField(populate_from='fullname', unique=True, blank=True)
    picture = models.ImageField(max_length=200, upload_to='teachers/',
                                verbose_name="O'qituvchi rasmi", null=False,
                                blank=False)
    fullname = models.CharField(max_length=200, null=False, blank=False,
                                verbose_name="O'qituvchi FIOsi")
    content = models.TextField(verbose_name="O'qituvchi haqida ma'lumot", null=False, blank=False)
    telegram = models.CharField(max_length=100, null=True, blank=True,
                                verbose_name="Telegram manzili")
    facebook = models.CharField(max_length=100, null=True, blank=True,
                                verbose_name="Facebook manzili")
    linkedin = models.CharField(max_length=100, null=True, blank=True,
                                verbose_name="LinkedIn manzili")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.fullname)

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.picture:
            self.picture.delete()
        super(Teachers, self).delete(*args, **kwargs)

    def __str__(self):
        return self.fullname

    def show_picture(self):
        return format_html(
            '<img src="{}" width="100" style="max-height:50px; object-fit: cover"/>'.format(self.picture.url))

    show_picture.short_description = "O'qituvchi rasmi"

    class Meta:
        verbose_name = "O'qituvchi "
        verbose_name_plural = "O'qituvhchilar "
