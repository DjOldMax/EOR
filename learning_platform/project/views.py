from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import StreamingHttpResponse
from .models import *
from .forms import *
from .ciphers import *
import random
from .services import open_file
from .example import *
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

value={
    'RSA':[],
    'Кузнечик':[],
    'MD5':[],
    'SHA256':[]
}

res_dict={
    'privkey':None,
    'res_encodeRSA':None
}
def post(request):
    global value
    try:
        # if request.method == 'POST' and request.POST['cipher']=='SHA256':
        #     name.clear()
        #     name.append(request.POST['cipher'])
        #     form1 = simulator_form()
        #     form2 = simulator_form_()
        #     return render(request,"project/cipher.html",{'ciphers':'','form1': form1, 'form2': form2, 'value':name[0]})
        # elif request.method == 'POST' and request.POST['cipher']=='MD5':
        if request.method == 'POST' and request.POST['cipher']=='RSA':
            value['RSA'].clear()
            value['RSA'].append(request.POST['cipher'])
            form1 = simulator_form()
            form2 = simulator_form_()
            return render(request,"project/cipher.html",{'ciphers':'RSA','form1': form1, 'form2': form2, 'value': value['RSA'][0]})
        elif request.method == 'POST' and request.POST['cipher']=='Кузнечик':
            value['Кузнечик'].clear()
            value['Кузнечик'].append(request.POST['cipher'])
            print(value)
            form1 = kuz_encode()
            form2 = kuz_decode()
            return render(request,"project/cipher.html",{'ciphers':'Кузнечик','form1': form1, 'form2': form2, 'value':value['Кузнечик'][0]})
        elif request.method == 'POST' or request.POST['cipher']=='MD5':
            value['MD5'].clear()
            value['MD5'].append(request.POST['cipher'])
            form = hash_form()
            return render(request,"project/cipher.html",{'ciphers':'MD5','form': form, 'value':value['MD5'][0]})
        elif request.method == 'POST' and request.POST['cipher']=='SHA256':
            value['SHA256'].clear()
            value['SHA256'].append(request.POST['cipher'])
            form = hash_form()
            return render(request,"project/cipher.html",{'ciphers':'SHA256','form': form, 'value': value['SHA256'][0]})
    except:  
        result=['','']    
        # ciphers_={
        #         'MD5':MD5_decrypt(request.POST['decrypt']),
        #         'SHA256':SHA256_decrypt(request.POST['decrypt']),
        #         'RSA':RSA_decrypt(request.POST['decrypt'],request.POST['privkey']),
        #         'Кузнечик':func_crypt(request.POST['decrypt'])
        #
        global res_dict               
        if request.method == 'POST' and request.POST['sub']=='run_сrypt_RSA':
            form1 = simulator_form(request.POST)
            form2 = simulator_form_(request.POST)
            # form = simulator_form(request.POST)
            result[0]=RSA_crypt(request.POST['crypt'])
            res_dict['res_encodeRSA'] = result[0][0]
            res_dict['privkey'] = result[0][1]
            return render(request,"project/cipher.html",{'ciphers':'RSA','form1': form1, 'form2': form2,'post1':result[0],'post2':result[1],'value':'RSA'})
        elif request.method == 'POST' and request.POST['sub']=='run_decrypt_RSA':
            form1 = simulator_form(request.POST)
            form2 = simulator_form_(request.POST)
            # print(tuple(request.POST['privkey'].split(',')))
            # res = request.POST['decrypt'][2:-1].encode('utf-8')
            # print(res)
            # print(type(res))
            # print(type(request.POST['decrypt']))
            # print(RSA_decrypt(res,tuple(request.POST['privkey'].split(','))))
            val = res_dict['res_encodeRSA']
            privkey = res_dict['privkey']
            print(res_dict['res_encodeRSA'])
            print(type(res_dict['res_encodeRSA']))
            print(res_dict['privkey'])
            print(type(res_dict['privkey']))
            res = RSA_decrypt(val, privkey)
            return render(request,"project/cipher.html",{'ciphers':'RSA','form1': form1, 'form2': form2,'post1':'','post2':res,'value':'RSA'})
        elif (request.method == 'POST') and (request.POST['sub']=='Crypt_KUZ'):
            form1 = kuz_encode(request.POST)
            form2 = kuz_decode(request.POST)
            post1 = func_crypt(request.POST['text'],request.POST['pswrd'])
            # post2 = func_encrypt(request.POST['crypto'],request.POST['keys'].split(','))
            # form = simulator_form(request.POST)
            print(request.POST['sub'])
            context={
                'form1': form1,
                 'form2': form2,
                 'post1':post1[0],
                 'keys':post1[1],
                 'post2':'',
                 'value':'Кузнечик',
                 'ciphers':'Кузнечик'
            }
            return render(request,"project/cipher.html",context=context)
        elif request.method == 'POST' and request.POST['sub']=='Decrypt_KUZ':
            print(len(request.POST['keys'].split(',')))
            print(request.POST['keys'].split(','))
            form1 = kuz_encode(request.POST)
            form2 = kuz_decode(request.POST)
            # post1 = func_crypt(request.POST['text'],request.POST['pswrd'])
            post2 = func_encrypt(request.POST['crypto'],request.POST['keys'].split(','))
            # form = simulator_form(request.POST)
            print(request.POST['sub'])
            context={
                'form1': form1,
                 'form2': form2,
                 'post2':post2,
                 'value':'Кузнечик',
                 'ciphers':'Кузнечик'
            }
            return render(request,"project/cipher.html",context=context)
        elif request.POST['sub']=='run_crypt_MD5':
            form = hash_form(request.POST)
            result = MD5_crypt(request.POST['hash'])
            context={
                'form':form,
                'result':result,
                'value':'MD5',
                'ciphers':'MD5'
            }
            return render(request,"project/cipher.html",context=context)
        elif request.method == 'POST' and request.POST['sub']=='run_crypt_SHA256':
            form = hash_form(request.POST)
            result = SHA256_crypt(request.POST['hash'])
            context={
                'form':form,
                'result':result,
                'value':'SHA256',
                'ciphers':'SHA256'
            }
            return render(request,"project/cipher.html",context=context)
        else:
            return HttpResponse('ошибка')






