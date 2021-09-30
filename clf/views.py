from datetime import datetime, time
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.db.models.query import QuerySet
from django.http import request
from django.http.request import QueryDict
from sklearn.linear_model import LinearRegression

import pickle
from django.shortcuts import render
from django import template
from django.template import loader
from django.http import HttpResponse
import os
from .models import entries
from .prediction import get_result,get_clf_info
# Create your views here.

def home(request):
    return render(request,'home.html')

def login_page(request):
    if request.method == 'GET':
        return render(request,'login.html')

def predict(request):
    type_clf = request.GET.get('type','')
    v1 = request.GET.get('v1','')
    v2 = request.GET.get('v2','')
    v3 = request.GET.get('v3','')
    v4 = request.GET.get('v4','')
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    if v1 == '' or v2 == '' or v3 == '' or v4 == '':
        result = 'please enter a values'
    elif type_clf == 'logistic':

        result = get_result(int(v1),int(v2),int(v3),int(v4))
        model_entry = entries()
        A = entries.objects.create(v1=v1,v2=v2,v3=v3,v4=v4,the_kind=result,prediction_time=current_time)
        result = 'the result is :' + result
    else:
        A = entries.objects.create(the_kind='not yet',prediction_time=current_time)
        result = 'we do not have this kind of service right now'
    
    context = {'result': result}
    template = 'result.html'
    return render(request,template,context)

def get_clfinfo(request):
    if request.method == 'GET':
        info = get_clf_info()
        template = 'info.html'
        return render(request,template,{'info' : info })

def login_user(request):
    template = 'login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        print(user)
        if user is None :
            context = {"error" : 'invalid username or password'}
            return render(request,template,context)        
        else :
            login(request,user)
            return redirect('/admin')
    return render(request,template,context)

def error(request):

    X = request.META.get('PATH_INFO',None).strip('/')
    return HttpResponse("<html><body><h1>there is no %s url </h1></body></html>"%(str(X)))