from django.contrib import admin

from django.contrib import admin
from .models import Listening, Reading, Test, Question, Option, Writing, Speaking

@admin.register(Listening)
class ListeningAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'submitters')
    search_fields = ('title', 'description')
    list_filter = ('language',)

@admin.register(Reading)
class ReadingAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'submitters')
    search_fields = ('title', 'description')
    list_filter = ('language',)

@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'listening', 'reading', 'order')
    search_fields = ('title', 'description', 'text', 'options', 'constraints')
    list_filter = ('listening', 'reading')


class OptionInline(admin.TabularInline):
    model = Option
    extra = 1

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'test', 'has_options')
    search_fields = ('text', 'answer')
    list_filter = ('test', 'has_options')
    inlines = [OptionInline]

# @admin.register(Option)
# class OptionAdmin(admin.ModelAdmin):
#     list_display = ('text', 'question', 'is_correct')
#     search_fields = ('text',)
#     list_filter = ('question', 'is_correct')

@admin.register(Writing)
class WritingAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'submitters')
    search_fields = ('title', 'description', 'task1', 'task2')
    list_filter = ('language',)

@admin.register(Speaking)
class SpeakingAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'submitters')
    search_fields = ('title', 'description')
    list_filter = ('language',)
