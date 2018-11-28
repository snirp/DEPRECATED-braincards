from django.contrib import admin

from ..models import Question, Choice, Answer


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('user', 'time', 'correct', 'question')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)