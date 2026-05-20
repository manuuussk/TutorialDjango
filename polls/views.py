from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import Question


def index(request):
    return HttpResponse("Página inicial das enquetes")


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse("Resultados da enquete")


def vote(request, question_id):
    return HttpResponse("Votação da enquete")