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
        return f'{self.word}'

    class Meta:
        verbose_name = 'Слово для изучения'
        verbose_name_plural = 'Слова для изучения'


class Exercise(models.Model):
    words = models.ManyToManyField(Word, verbose_name="Слова")
    student = models.ForeignKey(
        'auth.user', on_delete=models.CASCADE, related_name='exer_student', null=True, verbose_name='Ученик')
    teacher = models.ForeignKey(
        'auth.user', on_delete=models.CASCADE, related_name='exer_teacher', null=True, verbose_name="Учитель")
    is_active = models.BooleanField(default=True, verbose_name="Активен")
    
    def get_words(self):
        words = [str(word) for word in self.words.all()]
        return ', '.join(words)

    # def get_teachers(self):
    #     teachers = [user for user in User.objects.all() if user.groups.filter(name='Teacher').exists()]
    #     return ' '.join(teachers)

    def __str__(self) -> str:
        status = 'Active' if self.is_active else 'Done'
        return f"{self.id} - {self.student.last_name} {self.student.first_name} - {status}"

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
