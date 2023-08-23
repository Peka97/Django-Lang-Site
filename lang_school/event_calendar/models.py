from django.db import models

# Create your models here.


class EventModel(models.Model):
    title = models.CharField(max_length=50)
    time = models.DateTimeField()
    is_active = models.BooleanField(default=True)
    student = models.ForeignKey('auth.user', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student.last_name} {self.student.first_name} - {self.title}'

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'
