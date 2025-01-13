from django.db import models
from main.models import Language


class Listening(models.Model):
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, verbose_name="Til")
    title = models.CharField(max_length=150, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif", null=True, blank=True)
    submitters = models.IntegerField(default=0, verbose_name="Yuboruvchilar soni")

    def __str__(self):
        return self.title


class Reading(models.Model):
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, verbose_name="Til")
    title = models.CharField(max_length=150, verbose_name="Sarlavha")
    description = models.TextField(verbose_name="Tavsif", null=True, blank=True)
    submitters = models.IntegerField(default=0, verbose_name="Yuboruvchilar soni")

    def __str__(self):
        return self.title

class Test(models.Model):
    listening = models.ForeignKey(Listening, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Listening")
    reading = models.ForeignKey(Reading, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Reading")
    title = models.CharField(max_length=150, verbose_name="Sarlavha", null=True, blank=True)
    description = models.TextField(verbose_name="Tavsif", null=True, blank=True)
    picture = models.ImageField(upload_to='tests/pictures/', null=True, blank=True, verbose_name="Rasm")
    audio = models.FileField(upload_to='tests/audio/', null=True, blank=True, verbose_name="Audio")
    text_title = models.CharField(max_length=255, verbose_name="Matn sarlavhasi", null=True, blank=True)
    text = models.TextField(verbose_name="Test matni", null=True, blank=True)
    options = models.TextField(verbose_name="Variantlar", null=True, blank=True)
    sample = models.TextField(verbose_name="Misol", null=True, blank=True)
    constraints = models.TextField(verbose_name="Shartlar", null=True, blank=True)
    order = models.PositiveSmallIntegerField()

    def __str__(self):
        if self.title:
            return self.title
        elif self.description:
            return self.description
        elif self.text_title:
            return self.text_title
        elif self.constraints:
            return self.constraints
        else:
            return str(self.id)


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name="Savol testi")
    text = models.TextField(verbose_name="Savol matni")
    picture = models.ImageField(upload_to='questions/', null=True, blank=True, verbose_name="Rasm")
    answer = models.CharField(max_length=150, null=True, blank=True, verbose_name="Javob")
    has_options = models.BooleanField(default=True, verbose_name="Variantlar mavjud")

    class Meta:
        verbose_name = "Savol"
        verbose_name_plural = "Savollar"

    def __str__(self):
        return self.text

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name="Variant savoli")
    text = models.TextField(verbose_name="Variant")
    is_correct = models.BooleanField(default=False, verbose_name="To'g'ri variant")

    class Meta:
        verbose_name = "Variant"
        verbose_name_plural = "Variantlar"

    def __str__(self):
        return self.text


class Writing(models.Model):
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, verbose_name="Til")
    title = models.CharField(max_length=150, verbose_name="Sarlavha")
    picture = models.ImageField(upload_to='writing/', verbose_name="Rasm", null=True, blank=True)
    description = models.TextField(verbose_name="Tavsif", null=True, blank=True)
    task1 = models.TextField()
    task2 = models.TextField()
    submitters = models.IntegerField(default=0, verbose_name="Yuboruvchilar soni")

    def __str__(self):
        return self.title

class Speaking(models.Model):
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, verbose_name="Til")
    title = models.CharField(max_length=150, verbose_name="Sarlavha")
    picture = models.ImageField(upload_to='speaking/', verbose_name="Rasm")
    description = models.TextField(verbose_name="Tavsif")
    submitters = models.IntegerField(default=0, verbose_name="Yuboruvchilar soni")

    def __str__(self):
        return self.title


class UserTest(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE, verbose_name="Foydalanuvchi")
    language = models.ForeignKey(Language, on_delete=models.SET_NULL, null=True, verbose_name="Til")
    listening = models.ForeignKey(Listening, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Listening")
    done_listening = models.BooleanField(default=False)
    listening_result = models.PositiveSmallIntegerField(default=0, verbose_name="Listening natijasi")
    listening_user_options = models.JSONField(null=True, blank=True)
    reading = models.ForeignKey(Reading, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Reading")
    done_reading = models.BooleanField(default=False)
    reading_result = models.PositiveSmallIntegerField(default=0, verbose_name="Reading natijasi")
    reading_user_options = models.JSONField(null=True, blank=True)
    writing = models.ForeignKey(Writing, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Writing")
    done_writing = models.BooleanField(default=False)
    result = models.PositiveSmallIntegerField(default=0, verbose_name="Writing natijasi")
    writing_user_options = models.JSONField(null=True, blank=True)
    speaking = models.ForeignKey(Speaking, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Speaking")
    done_speaking = models.BooleanField(default=False)
    speaking_result = models.PositiveSmallIntegerField(default=0, verbose_name="Speaking natijasi")
    speaking_user_options = models.JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

