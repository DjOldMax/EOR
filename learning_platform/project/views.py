from django.shortcuts import render, get_object_or_404
from django.http import StreamingHttpResponse
from .models import *
import random
from .services import open_file
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

    return render(request, 'project/index.html', context = context)


def show_book(request, book_id):
    context={
        'book_id':str(book_id)
    }
    return render(request, 'project/book.html', context=context)

def show_media(request):
    context={
        "video_list": VIDEOS.objects.all()
    }
    return render(request, 'project/video_list.html',context=context)

def show_video(request,pk: int):
    _video = get_object_or_404(VIDEOS, id=pk)
    return render(request, "project/video_stream.html", {"video": _video})

def stream_video(request,pk:int):
    file, status_code, content_length, content_range = open_file(request, pk)
    response = StreamingHttpResponse(file, status=status_code, content_type='video/mp4')

    response['Accept-Ranges'] = 'bytes'
    response['Content-Length'] = str(content_length)
    response['Cache-Control'] = 'no-cache'
    response['Content-Range'] = content_range
    return response

def show_kurs(request):
    return render(request,"project/cryptography.html")




