from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Poll

def create_page(request):
    if request.method == 'POST':
        print(request.POST)
        poll = Poll(request.POST)
        question_1 = request.POST.get('question_1')
        question_2 = request.POST.get('question_2')
        poll = Poll(
            question_1=question_1,
            question_2=question_2,
            )
        print(poll)
        poll.save()
        print('poll', poll)
        poll_id = poll.id
        print('poll_id', poll_id)
        return HttpResponseRedirect('/responses/' + str(poll_id))
    else:
        return render(request, 'create.html', {
        })

def responses_page(request, poll_id):
    poll = Poll.objects.get(id=int(poll_id))
    return render(request, 'responses.html', {
        'name': 'hello',
        'poll_id': poll_id,
        'poll': poll,
        })

def answer_page(request, poll_id):
    poll = Poll.objects.get(id=int(poll_id))
    questions = Questions.find(poll_id=poll_id)
    return render(request, 'answer.html', {
        'name': 'hello',
        'poll_id': poll_id,
        'questions': questions
        })

