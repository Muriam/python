from django.shortcuts import render       # для шаблонов
# from django.http import HttpResponse      #  для request, HttpResponse чтоб получать ответ
from .models import Dictionary


def posts(request):
    return render(request, 'main/index.html')


def grammar(request):
    return render(request, 'main/grammar.html')


def dictionary(request):
    words = Dictionary.objects.all()
    return render(request, 'main/dictionary.html', {"words": words})


def books(request):
    return render(request, 'main/books.html')


def django(request):
    return render(request, 'main/django.html')


def flask(request):
    return render(request, 'main/flask.html')