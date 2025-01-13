from django.db import models
from django.utils.html import format_html

from main.models import Language


class Direction(models.Model):
    picture = models.ImageField(upload_to='directions/', verbose_name="Rasm")
    title = models.CharField(max_length=150, verbose_name="Sarlavha")
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, verbose_name="Til")
    mark = models.IntegerField(default=0, verbose_name="Bahosi")
    learners = models.IntegerField(default=0, verbose_name="O'quvchilar soni")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Delete the old image file if it is being replaced
        if self.pk:
            old_instance = Direction.objects.get(pk=self.pk)
            if old_instance.picture and old_instance.picture != self.picture:
                old_instance.picture.delete(save=False)
        super().save(*args, **kwargs)

    def show_picture(self):
        if self.picture:
            return format_html(
                '<img src="{}" width="100" style="max-height:50px; object-fit: cover;" />',
                self.picture.url
            )
        return "(No Image)"
    show_picture.short_description = "Yo'nalish rasmi"


class Exam(models.Model):
    title = models.CharField(max_length=150, verbose_name="Sarlavha")
    picture = models.ImageField(upload_to='exams/', verbose_name="Rasm")
    text = models.TextField(verbose_name="Imtixon matni", null=True, blank=True)
    description = models.TextField(verbose_name="Tavsif")
    direction = models.ForeignKey(Direction, on_delete=models.SET_NULL, null=True, verbose_name="Yo'nalish")
    # listening = models.ForeignKey(Listening, on_delete=models.SET_NULL, null=True, verbose_name="Listening")
    # reading = models.ForeignKey(Reading, on_delete=models.SET_NULL, null=True, verbose_name="Reading")
    submitters = models.IntegerField(default=0, verbose_name="Yuboruvchilar soni")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Delete the old image file if it is being replaced
        if self.pk:
            old_instance = Exam.objects.get(pk=self.pk)
            if old_instance.picture and old_instance.picture != self.picture:
                old_instance.picture.delete(save=False)
        super().save(*args, **kwargs)

    def show_picture(self):
        if self.picture:
            return format_html(
                '<img src="{}" width="100" style="max-height:50px; object-fit: cover;" />',
                self.picture.url
            )
        return "(No Image)"
    show_picture.short_description = "Imtihon rasmi"


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE, verbose_name="Savol testi")
    text = models.TextField(verbose_name="Savol matni")
    picture = models.ImageField(upload_to='questions/', null=True, blank=True, verbose_name="Rasm")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Savol"
        verbose_name_plural = "Savollar"


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Variant savoli")
    text = models.TextField(verbose_name="Variant")
    is_correct = models.BooleanField(default=False, verbose_name="To'g'ri variant")

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Variant"
        verbose_name_plural = "Variantlar"



class QuizLog(models.Model):
    json = models.JSONField()