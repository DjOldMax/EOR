from django.shortcuts import render
from .models import *
import random
# Create your views here.

def home(request):
    books=[i for i in BOOKS.objects.all()]
    test_list=[i for i in TEST.objects.all()]
#     context={
#         'books':books,
#         'value':[
#     {
#     'numb': 1,
#     'question': "What does HTML stand for?",
#     'answer': "Hyper Text Markup Language",
#     'options': [
#       "Hyper Text Preprocessor",
#       "Hyper Text Markup Language",
#       "Hyper Text Multiple Language",
#       "Hyper Tool Multi Language"
#     ]
#    },
#     {
#     'numb': 2,
#     'question': "What does CSS stand for?",
#     'answer': "Cascading Style Sheet",
#     'options': [
#       "Common Style Sheet",
#       "Colorful Style Sheet",
#       "Computer Style Sheet",
#       "Cascading Style Sheet"
#     ]
#    },
#     {
#     'numb': 3,
#     'question': "What does PHP stand for?",
#     'answer': "Hypertext Preprocessor",
#     'options': [
#       "Hypertext Preprocessor",
#       "Hypertext Programming",
#       "Hypertext Preprogramming",
#       "Hometext Preprocessor"
#     ]
#    },
#     {
#     'numb': 4,
#     'question': "What does SQL stand for?",
#     'answer': "Structured Query Language",
#     'options': [
#       "Stylish Question Language",
#       "Stylesheet Query Language",
#       "Statement Question Language",
#       "Structured Query Language"
#     ]
#    },
#     {
#     'numb': 5,
#     'question': "What does XML stand for?",
#     'answer': "eXtensible Markup Language",
#     'options': [
#       "eXtensible Markup Language",
#       "eXecutable Multiple Language",
#       "eXTra Multi-Program Language",
#       "eXamine Multiple Language"
#     ]
#    }]

    # }
    context={
        'books':books,
        'value':[]
    }
    for i in test_list:

        other = {}
        other['numb'] = i.pk
        other['question'] = i.question
        other['answer'] = i.answer0
        answer=[i.answer0,i.answer1,i.answer2,i.answer3]
        random.shuffle(answer)
        other['options'] = answer
        context['value'].append(other)
    print(context['value'])
    return render(request, 'project/index.html', context = context)


def show_book(request, book_id):
    context={
        'book_id':str(book_id)
    }
    return render(request, 'project/book.html', context=context)



