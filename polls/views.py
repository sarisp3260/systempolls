from ast import For
from re import template
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import FormView
from .forms import CreateAnswerForm, CreatePollForm
from .models import Poll, Answers, Votes
from django.forms import formset_factory

def home(request):
    polls = Poll.objects.all()
    context = {
        'polls' : polls
    }
    return render(request, 'poll/home.html', context)

def create(request):
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = CreatePollForm()
    context = {
        'form' : form
    }
    return render(request, 'poll/create.html', context)

def create2(request):
    
 
    if request.method == 'POST':
        form = CreatePollForm(request.POST)
        form2= request.POST
        print(form2['form-TOTAL_FORMS'])
        print("-------------------------------")
        print("data:",form2)
       

        if form.is_valid():
            #for f in form:
            print(form.cleaned_data['question'])
            poll=form.save()
            print(poll.id)
            for i in range(int(form2['form-TOTAL_FORMS'])):
                var="form-"+str(i)+"-option"
                answers= Answers()
                answers.option=form2[var]
                answers.poll_id=poll.id
                print(answers)
                answers.save()
            return redirect('home')
    else:
        form = CreatePollForm()
        form2= formset_factory(CreateAnswerForm, extra=3)
    context = {
        'form' : form,
        'form2': form2
    }
    return render(request, 'poll/create2.html', context)

def vote(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)

    if request.method == 'POST':

        selected_option = request.POST['poll']
        if selected_option == 'option1':
            poll.option_one_count += 1
        elif selected_option == 'option2':
            poll.option_two_count += 1
        elif selected_option == 'option3':
            poll.option_three_count += 1
        else:
            return HttpResponse(400, 'Invalid form')

        poll.save()

        return redirect('results', poll.id)

    context = {
        'poll' : poll
    }
    return render(request, 'poll/vote.html', context)

def vote2(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    answers = Answers.objects.filter(poll_id=poll_id)
    print(answers[0])
    if request.method == 'POST':

        selected_option = request.POST['poll']
        print(selected_option)
        for i in answers:
            print(i.id == int(selected_option))
            if i.id == int(selected_option):
                vote= Votes()
                vote.poll_id=poll.id
                vote.answer_id=i.id
                vote.save()

        return redirect('results', poll.id)

    context = {
        'poll' : poll,
        'answers':answers
    }
    return render(request, 'poll/vote2.html', context)

def results(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    context = {
        'poll' : poll
    }
    return render(request, 'poll/results.html', context)

def results2(request, poll_id):
    poll = Poll.objects.get(pk=poll_id)
    answers = Answers.objects.filter(poll_id=poll_id)
    votes=Votes.objects.filter(poll_id=poll_id).count()
    print(answers)
    context = {
        'poll' : poll,
        'answers':answers,
        'votes':votes
    }
    return render(request, 'poll/results2.html', context)
