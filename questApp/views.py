from django.shortcuts import render
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied

from .models import Question, Answer
from .forms import QuestionForm, AnswerForm



def index(request):
    """Домашняя страница"""
    return render(request, "questApp/index.html")

def questions(request):
    """Отображает список всех вопросов"""
    questions = Question.objects.order_by('date_added')
    context = {'questions': questions}
    return render(request, "questApp/questions.html", context)

@login_required()
def answers(request, question_id):
    """Отображает все ответы на вопрос"""
    question = Question.objects.get(id=question_id)
    answers = question.answer_set.order_by('-date_added')
    context = {'question': question, 'answers': answers}
    return render(request, "questApp/answers.html", context)

@login_required()
def new_question(request):
    """Выводит форму для нового вопроса"""
    if request.method != 'POST':
        # Если данные не отправлялись, то нужно вывести пустую форму
        form = QuestionForm()
    else:
        form = QuestionForm(request.POST)  # Передаём данные, храняшиеся в реквесте, в экземпляр
        if form.is_valid():  # Проверяем, всё ли заполнено правильно
            new_question = form.save(commit=False)  # Записываем данные в БД
            new_question.owner = request.user
            new_question.save()
            return HttpResponseRedirect(reverse('questApp:questions'))  # Перенаправляем на страницу с вопросами

    context = {'form': form}
    return render(request, "questApp/new_question.html", context)

@login_required()
def new_answer(request, question_id):
    """Выводит форму для ответа на конкретный вопрос"""
    question = Question.objects.get(id=question_id)  # Получаем объект конкретного вопроса

    if request.method != 'POST':
        form = AnswerForm()
    else:
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            new_answer = form.save(commit=False)  # сохраняем, но не коммитим
            new_answer.question = question
            new_answer.save()
            return HttpResponseRedirect(reverse('questApp:answers', args=[question_id]))

    context = {'question': question, 'form': form}
    return render(request, "questApp/new_answer.html", context)

@login_required()
def edit_answer(request, answer_id):
    """Редактирование существующего ответа"""
    answer = Answer.objects.get(id=answer_id)
    question = answer.question
    if question.owner != request.user:
        raise PermissionDenied

    if request.method != 'POST':
        form = AnswerForm(instance=answer)  # Исходный запрос, форма заполняется текущими данными
    else:
        form = AnswerForm(instance=answer, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('questApp:answers', args=[question.id]))

    context = {'answer': answer, 'question': question, 'form': form}
    return render(request, 'questApp/edit_answer.html', context)

@login_required()
def edit_question(request, question_id):
    """Редактирование существующего ответа"""
    question = Question.objects.get(id=question_id)

    if question.owner != request.user:
        raise PermissionDenied

    if request.method != 'POST':
        form = QuestionForm(instance=question)  # Исходный запрос, форма заполняется текущими данными
    else:
        form = QuestionForm(instance=question, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('questApp:answers', args=[question.id]))

    context = {'question': question, 'form': form}
    return render(request, 'questApp/edit_question.html', context)






