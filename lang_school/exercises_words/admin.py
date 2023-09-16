from django.contrib import admin

from .models import Word, Exercise, ExerciseResult

# Register your models here.

admin.site.register(Word)
admin.site.register(Exercise)
admin.site.register(ExerciseResult)
