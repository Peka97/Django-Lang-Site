from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from .models import Word, Exercise, ExerciseResult


# Filters
# class RoleFilter(admin.SimpleListFilter):
#     title = _('Роль')
#     # Parameter for the filter that will be used in the URL query.
#     parameter_name = "groups"

#     def lookups(self, request, model_admin):
#         teachers = [user for user in set(User.objects.all()) if user.groups.filter(name='Teacher').exists()]
        
#         return teachers

#     def queryset(self, request, queryset):
#         if self.value():
#             return queryset.filter(teacher=self.value())
    


# Register your models here.

admin.site.register(Word)
# admin.site.register()
admin.site.register(ExerciseResult)


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('teacher', 'student' , 'is_active', 'get_words')
    list_display_links = ('student', 'teacher')
    list_filter = ('teacher', 'student', 'is_active')
    search_fields = ('teacher__username', )
