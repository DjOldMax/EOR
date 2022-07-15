from django.shortcuts import render, get_object_or_404
from django.http import StreamingHttpResponse
from .models import *
from .forms import *
from .ciphers import *
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

def get_simulators(request):
    request.GET.get('id')
    return render(request,"project/simulators.html")

name=[]
def post(request):
    post=''
    ciphers={
        'MD5':'',
        'SHA256':''
    }
    try:
        if request.method == 'POST' and request.POST['cipher']=='SHA256':
            name.clear()
            name.append(request.POST['cipher'])
            form = simulator_form()
            return render(request,"project/cipher.html",{'ciphers':'','form': form, 'value':name[0]})
        # elif request.method == 'POST' and request.POST['cipher']=='MD5':
        else:
            name.clear()
            name.append(request.POST['cipher'])
            form = simulator_form()
            return render(request,"project/cipher.html",{'ciphers':'','form': form, 'value':name[0]})
    except:
        if request.method == 'POST' and request.POST['sub']=='run':
            ciphers={
                'MD5':MD5(request.POST['text']),
                'SHA256':SHA256(request.POST['text'])
            }
            form = simulator_form(request.POST)
            post=ciphers[name[0]]
            return render(request,"project/cipher.html",{'form': form,'post':post,'value':name[0]})
        else:
            form = simulator_form()
            return render(request,"project/cipher.html",{'ciphers':ciphers[name],'form': form,'value':name[0]})






