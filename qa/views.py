from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.core.paginator import Paginator
from taggit.models import Tag
from .models import *
from .forms import *

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def index(request):
    questions = Question.objects.new()
    limit = request.GET.get('limit', 5)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    context = {'questions': page.object_list, 'paginator': paginator, 
                'page': page, 'order': 'new'}
    return render(request, 'index.html', context)

def popular (request):
    questions = Question.objects.popular()
    limit = request.GET.get('limit', 5)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = '/popular/?page='
    page = paginator.page(page)
    context = {'questions': page.object_list, 'paginator': paginator, 
                'page': page, 'order': 'popular'}
    return render(request, 'index.html', context)

def tagged (request, slug):
    tag = get_object_or_404(Tag, slug=slug)
    questions = Question.objects.popular().filter(tags=tag)
    limit = request.GET.get('limit', 5)
    page = request.GET.get('page', 1)
    paginator = Paginator(questions, limit)
    paginator.baseurl = f'/tagged/{slug}/?page='
    page = paginator.page(page)
    context = {'questions': page.object_list, 'paginator': paginator, 
                'page': page, 'tag_filter': tag}
    return render(request, 'index.html', context)


def question(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answer_set.order_by('-added_at')
    if request.method != 'POST':
        form = AnswerForm()
    else:
        form = AnswerForm(data=request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.question = question
            answer.author = request.user
            answer.save()
            url = question.get_url()
            return redirect(url)
    context = {'question': question, 'answers': answers, 'form': form}
    return render(request, 'question.html', context)

@login_required
def ask(request):
    if request.method != 'POST':
        form = AskForm()
    else:
        form = AskForm(data=request.POST)
        if form.is_valid():
            ask = form.save(commit=False)
            ask.author = request.user
            ask.save()
            form.save_m2m()
            url = ask.get_url()
            return redirect(url)
    context = {'form': form}
    return render(request, 'ask.html', context)

@login_required
def question_like(request, **kwargs):
    url_from = request.POST.get('url_from')
    question_id = request.POST.get('question_id')
    question = get_object_or_404(Question, id=question_id)
    if request.method == 'POST':
        user = request.user
        if question.likes.filter(id=user.id):
            question.likes.remove(user)
        else:
            question.likes.add(user)
    return redirect(url_from)

@login_required
def answer_like(request, **kwargs):
    url_from = request.POST.get('url_from')
    answer_id = request.POST.get('answer_id')
    answer = get_object_or_404(Answer, id=answer_id)
    if request.method == 'POST':
        user = request.user
        if answer.likes.filter(id=user.id):
            answer.likes.remove(user)
        else:
            answer.likes.add(user)
    return redirect(url_from)

@login_required
def answer_correct(request, **kwargs):
    answer_id = request.POST.get('answer_id')
    answer = get_object_or_404(Answer, id=answer_id)
    question = answer.question
    if request.method == 'POST' and request.user == question.author:
        answer.is_correct = not answer.is_correct
        answer.save()
    return redirect(question.get_url())