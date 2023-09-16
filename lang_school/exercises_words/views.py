import json
from random import sample, shuffle

from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Exercise, Word, ExerciseResult

# Create your views here.


def exercises_words(request, id, step):
    print(step)
    user_login = request.user
    try:
        exercise = list(Exercise.objects.filter(
            id=id,
            student=user_login
        ).all())[0]
    except IndexError:
        return redirect('profile')
    words = get_words(exercise)

    template_name = f'exercises_words/exercise_step_{step}.html'
    context = {
        'id': id,
        'step': step,
        'words': words,
        'shuffled_translates': get_shuffled_translates(list(exercise.words.all())),
        'len': range(1, len(words) + 1)
    }
    return render(request, template_name, context)


def get_words(exercise: list[Exercise]):
    result = []
    words = list(exercise.words.all())

    for idx, word in enumerate(words):
        data = {
            'id': idx + 1,
            'word': word.word,
            'translate': word.translate,
            'sentences': word.sentences.split('\n'),
            'translate_vars': get_translate_vars(words, word),
        }
        result.append(data)

    return result


def get_shuffled_translates(words: list[Word]) -> list[dict]:
    translates = [{'id': idx + 1, 'trans': word.translate}
                  for idx, word in enumerate(words)]
    shuffle(translates)
    return translates


def get_translate_vars(words: list[Word], word: str):
    ex_words = [word.translate for word in words]
    del ex_words[ex_words.index(word.translate)]

    words = sample(ex_words, 3)
    words.append(word.translate)
    shuffle(words)
    return words


def update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        exercise_id = data.get('exercise_id')
        step = data.get('step')
        value = data.get('value')
        obj, is_created = ExerciseResult.objects.get_or_create(
            exercise=Exercise.objects.get(pk=exercise_id),
            step=step,
            result=value
        )
        if is_created:
            try:
                obj.save()
            except Exception:
                print('Ошибка добавления')

        return HttpResponse(status=200)
    return HttpResponse(status=404)
