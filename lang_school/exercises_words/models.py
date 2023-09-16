from django.db import models

# Create your models here.


class Word(models.Model):
    word = models.CharField(max_length=50)
    translate = models.CharField(max_length=255)
    lang = models.CharField(
        max_length=10,
        default='eng',
        choices=[
            ('eng', 'English'),
            ('fr', 'French'),
            ('sp', 'Spanish')
        ]
    )
    sentences = models.TextField(max_length=255, null=True, blank=True)

    def __str__(self) -> str:
        return f'{self.word} - {self.lang}'

    class Meta:
        verbose_name = 'Слово для изучения'
        verbose_name_plural = 'Слова для изучения'


class Exercise(models.Model):
    words = models.ManyToManyField(Word)
    student = models.ForeignKey(
        'auth.user', on_delete=models.CASCADE, related_name='exer_student', null=True)
    teacher = models.ForeignKey(
        'auth.user', on_delete=models.CASCADE, related_name='exer_teacher', null=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.student}"

    class Meta:
        verbose_name = 'Упражнение'
        verbose_name_plural = 'Упражнения'


class ExerciseResult(models.Model):
    exercise = models.ForeignKey(
        Exercise, on_delete=models.CASCADE, related_name='exercise_result', null=True)
    step = models.CharField(
        max_length=25,
        choices=[
            ('1', 'Step 1'),
            ('2', 'Step 2'),
            ('3', 'Step 3'),
            ('4', 'Step 4'),
        ]
    )
    result = models.SmallIntegerField()

    def __str__(self) -> str:
        return f'{self.exercise.student} - {self.exercise.id} - {self.step}'

    class Meta:
        verbose_name = 'Результат упражнения'
        verbose_name_plural = 'Результаты упражнений'
