from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import Questions, UpDownVotesQuestion, UpDownVotesAnswer

def giris(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            temiz = form.cleaned_data
            user = authenticate(username=temiz['kulad'], password=temiz['parola'])
            if user is not None:
                login(request,user)
                return HttpResponseRedirect('/')
            else:
                return HttpResponseRedirect('/login')

    else:
        form = LoginForm
        return render(request,"login.html",locals())


def cikis(request):
    if request.user:
        logout(request)
    return HttpResponseRedirect("/")


def anasayfa(request):
    questions = Questions.objects.all()
    return render(request,"home.html", locals())


def yeni_soru(request):
    if request.method == 'POST':
        form = NewQuestion(request.POST)
        if form.is_valid():
            temiz = form.cleaned_data
            data = Questions(title=temiz['title'], user_id=request.user)
            data.save()
            return HttpResponseRedirect('/')
    else:
        form = NewQuestion()
        return render(request, 'newquestion.html', locals())


def soru_sayfasi(request, number):
    up = UpDownVotesQuestion.objects.filter(question_id=number,up_down=1).count()
    down = UpDownVotesQuestion.objects.filter(question_id=number,up_down=0).count()    
    question = Questions.objects.get(id=number)
    return render(request, 'question.html', locals())


def question_up(request, updown ,number):
    temp = UpDownVotesQuestion.objects.filter(question_id=number,user_id=request.user).count()
    question = Questions.objects.get(id=number)
    if temp == False:
        data = UpDownVotesQuestion(up_down=updown, question_id=question, user_id=request.user)
        data.save()
    else:
        temp = UpDownVotesQuestion.objects.get(question_id=number,user_id=request.user)
        if temp.up_down != updown:
                temp.up_down = updown
                temp.save()
    return HttpResponseRedirect("/question/{}".format(number))