from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return f'{self.pk} - {self.name}'
    
    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Review(models.Model):
    text = models.CharField(max_length=150)
    from_user = models.ForeignKey(
        'auth.user',
        
        on_delete=models.CASCADE,
        related_name='from_user'
        )
    datetime = models.DateTimeField(
        auto_now=True,
    )
    
    def __str__(self) -> str:
        return f'{self.pk} - {self.datetime.strftime("%d.%m.%Y")} - {self.from_user.first_name}'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'