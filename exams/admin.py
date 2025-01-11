from django.contrib import admin
from .models import Language, Direction, Exam, Question, Option


@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name', 'flag')
    search_fields = ('name',)


@admin.register(Direction)
class DirectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'language', 'mark', 'learners', 'show_picture')
    list_filter = ('language',)
    search_fields = ('title', 'language__name')
    readonly_fields = ('show_picture',)
    fieldsets = (
        (None, {
            'fields': ('title', 'picture', 'show_picture', 'language', 'mark', 'learners')
        }),
    )


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = ('title', 'direction', 'submitters', 'show_picture')
    list_filter = ('direction',)
    search_fields = ('title', 'direction__title')
    readonly_fields = ('show_picture',)
    inlines = [QuestionInline]
    fieldsets = (
        (None, {
            'fields': ('title', 'picture', 'show_picture', 'description', 'direction', 'submitters')
        }),
    )


class OptionInline(admin.TabularInline):
    model = Option
    extra = 1


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'exam')
    search_fields = ('text', 'exam__title')
    inlines = [OptionInline]
    fieldsets = (
        (None, {
            'fields': ('exam', 'text', 'picture')
        }),
    )


@admin.register(Option)
class OptionAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
    list_filter = ('is_correct',)
    search_fields = ('text', 'question__text')
