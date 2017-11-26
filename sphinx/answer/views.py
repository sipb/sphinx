from django.shortcuts import render
from django.http import HttpResponse

# TODO: get models for Poll, Responses

def create_page(request):
    return render(request, 'create.html', {
        })

def responses_page(request, poll_id):
    return render(request, 'responses.html', {
        'name': 'hello',
        'poll_id': poll_id,
        })

def answer_page(request, poll_id):
    return render(request, 'answer.html', {
        'name': 'hello',
        'poll_id': poll_id,
        })
