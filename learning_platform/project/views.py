from django.shortcuts import render
from .models import *
import random
# Create your views here.

def home(request):
    books=[i for i in BOOKS.objects.all()]
    test_list=[i for i in TEST.objects.all()]
    moduls=sorted(set([i.modul for i in TEST.objects.all()]))
    context={
        'books':books,
        'value':[],
        'moduls':moduls
    }
    for i in test_list:

        other = {}
        other['numb'] = i.pk
        other['modul'] = i.modul
        other['question'] = i.question
        other['answer'] = i.answer0
        answer=[i.answer0,i.answer1,i.answer2,i.answer3]
        random.shuffle(answer)
        other['options'] = answer
        context['value'].append(other)
    print(context['value'])
    print(moduls)
    return render(request, 'project/index.html', context = context)


def show_book(request, book_id):
    context={
        'book_id':str(book_id)
    }
    return render(request, 'project/book.html', context=context)

def show_media(request):
    return render(request, 'project/media.html')






