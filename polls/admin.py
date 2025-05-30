from django.contrib import admin

from polls.models import Question, Choice


# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    # fieldsets =
    list_display = ["question_text", "pub_date", "was_recent"]
    list_filter = ["create_date"]
    inlines = [ChoiceInline]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)
