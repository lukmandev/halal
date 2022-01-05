from django.contrib import admin
from .models import Question


class QuestionConfig(admin.ModelAdmin):

    list_filter = ('author', 'question', 'answer')
    search_fields = ('author', 'question', 'answer')
    list_display = ('id', 'author', 'question', 'answer')
    list_display_links = ('id', 'author')

    fieldsets = (
        ('Info', {'fields': ('author',)}),
        ('Question And Answer', {'fields': ('question', 'answer')})
    )


admin.site.register(Question, QuestionConfig)

