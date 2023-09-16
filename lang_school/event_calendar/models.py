from django.db import models

# Create your models here.


class EventModel(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255, null=True)
    datetime = models.DateTimeField()
    is_paid = models.BooleanField(default=True)
    status = models.CharField(
        max_length=10,
        default='P',
        choices=[
            ('P', 'planned'),
            ('M', 'missed'),
            ('D', 'done'),
            ('C', 'canceled')
        ]
    )
    student = models.ForeignKey(
        'auth.user', on_delete=models.CASCADE, related_name='event_student', null=True)
    teacher = models.ForeignKey(
        'auth.user', on_delete=models.CASCADE, related_name='event_teacher', null=True)

    def __str__(self):
        return f'{self.pk} - {self.datetime} - {self.student.last_name} {self.student.first_name} - {self.title}'

    class Meta:
        verbose_name = 'Занятие'
        verbose_name_plural = 'Занятия'

        ordering = ['-datetime']
