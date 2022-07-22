from django.shortcuts import render
from django.contrib.auth import authenticate,logout#,login
from django.contrib.auth import login as auth_login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from .models import GOAL22,FIG
from .forms import GOAL22Q1Form
import os

# Create your views here.

User = get_user_model()

def home(request):
    form = 'hello'
    return render(request, 'MBO/home.html', {'form': form})

def login(request):
    if request.method == 'POST':
        ID = request.POST.get('userid')
        Pass = request.POST.get('password')
        user = authenticate(username=ID, password=Pass)
        if user:
            if user.is_active:
                auth_login(request,user)
                #login(request,user)
                #return HttpResponseRedirect(reverse('sample'))
                return render(request, 'MBO/sample.html')
            else:
                return HttpResponse("アカウントが有効ではありません")
        else:
            return HttpResponse("ログインIDかパスワードに誤りがあります")
    else:
        return render(request, 'MBO/login.html')

def sample(request,num):

    params = {
        "foto" : FIG.objects.all(),
        }
    return render(request, 'MBO/sample.html', params)

def GOAL(request,num):
    params = {
        "UserID":request.user,
        "data1":GOAL22.objects.values_list('GOAL22A1','GOAL22B1','GOAL22C1','GOAL22D1','GOAL22E1','GOAL22F1','GOAL22G1').get(user=request.user),
        "data2":GOAL22.objects.values_list('GOAL22AP','GOAL22BP','GOAL22CP','GOAL22DP','GOAL22EP','GOAL22FP','GOAL22GP').get(user=request.user),
        "data3":GOAL22.objects.values_list('GOAL22A2','GOAL22B2','GOAL22C2','GOAL22D2','GOAL22E2','GOAL22F2','GOAL22G2').get(user=request.user),
        "data4":GOAL22.objects.values_list('GOAL22A3','GOAL22B3','GOAL22C3','GOAL22D3','GOAL22E3','GOAL22F3','GOAL22G3').get(user=request.user),
        "data5":GOAL22.objects.values_list('GOAL22AR','GOAL22BR','GOAL22CR','GOAL22DR','GOAL22ER','GOAL22FR','GOAL22GR').get(user=request.user),
        }
    return render(request, 'MBO/GOAL.html', params)

def edit(request, num):
    obj = GOAL22.objects.get(user=request.user)
    if (request.method == 'POST'):
        friend = GOAL22Q1Form(request.POST, instance=obj)
        friend.save()
        params = {
            "UserID":request.user,
            "data1":GOAL22.objects.values_list('GOAL22A1','GOAL22B1','GOAL22C1','GOAL22D1','GOAL22E1','GOAL22F1','GOAL22G1').get(user=request.user),
            "data2":GOAL22.objects.values_list('GOAL22AP','GOAL22BP','GOAL22CP','GOAL22DP','GOAL22EP','GOAL22FP','GOAL22GP').get(user=request.user),
            "data3":GOAL22.objects.values_list('GOAL22A2','GOAL22B2','GOAL22C2','GOAL22D2','GOAL22E2','GOAL22F2','GOAL22G2').get(user=request.user),
            "data4":GOAL22.objects.values_list('GOAL22A3','GOAL22B3','GOAL22C3','GOAL22D3','GOAL22E3','GOAL22F3','GOAL22G3').get(user=request.user),
            "data5":GOAL22.objects.values_list('GOAL22AR','GOAL22BR','GOAL22CR','GOAL22DR','GOAL22ER','GOAL22FR','GOAL22GR').get(user=request.user),
            }
        return render(request, 'MBO/GOAL.html', params)

    params = {
        "UserID":request.user,
        "data1":GOAL22Q1Form(instance=obj),
        "data2":GOAL22.objects.values_list('GOAL22A2','GOAL22B2','GOAL22C2','GOAL22D2','GOAL22E2','GOAL22F2','GOAL22G2').get(user=request.user),
        "data3":GOAL22.objects.values_list('GOAL22A3','GOAL22B3','GOAL22C3','GOAL22D3','GOAL22E3','GOAL22F3','GOAL22G3').get(user=request.user),
        "data4":GOAL22.objects.values_list('GOAL22AR','GOAL22BR','GOAL22CR','GOAL22DR','GOAL22ER','GOAL22FR','GOAL22GR').get(user=request.user),
        }
    return render(request, 'MBO/edit.html', params)
