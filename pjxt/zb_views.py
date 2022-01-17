import os
import json,requests
from django.views.decorators import csrf
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import auth
from django.http import JsonResponse
from django.core import serializers
from pjxt.models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.conf import settings

@csrf_exempt
def Fzb_viability(request):
    data=[]
    ctx ={}
    title=['YYY','XXX','PPP']
    ctx['dic']={'table_title':title,'data':data}
    return render(request, "pjxt/zb/viability.html", ctx)

@csrf_exempt
def viabilityupdate(request):
    data=json.loads(request.body)
    for i in data:
        if "id" in i:
            zb_viability.objects.filter(id=i['id']).update(**i)
        else:
            del i['row']
            zb_viability.objects.create(**i)
    return HttpResponse('200','application/json')

@csrf_exempt
def viabilityajax(request):
    pa1=request.POST['PA1']
    pa1=pa1[0:1]
    mydata=zb_viability.objects.filter(skillid__startswith=pa1).values().order_by("level","num")
    menus=[entry for entry in mydata]
    menus=list(menus)
    data=json.dumps(menus,ensure_ascii=False)
    return HttpResponse(data,'application/json')

@csrf_exempt
def viabilitylevel (request):
    mydata=zb_viability.objects.filter(level=1).values('skillid','text')
    menus=[entry for entry in mydata]
    menus=list(menus)
    data=json.dumps(menus,ensure_ascii=False)
    return HttpResponse(data,'application/json')

@csrf_exempt
def Fzb_strengthen(request):
    data=[]
    ctx ={}
    title=['YYY','XXX','PPP']
    ctx['dic']={'table_title':title,'data':data}
    return render(request, "pjxt/zb/strengthen.html", ctx)

@csrf_exempt
def strengthenupdate(request):
    data=json.loads(request.body)
    for i in data:
        if "id" in i:
            zb_strengthen.objects.filter(id=i['id']).update(**i)
        else:
            del i['row']
            zb_strengthen.objects.create(**i)
    return HttpResponse('200','application/json')

@csrf_exempt
def strengthenajax(request):
    pa1=request.POST['PA1']
    pa1=pa1[0:1]
    mydata=zb_strengthen.objects.filter(sid__startswith=pa1).values().order_by("level","num")
    menus=[entry for entry in mydata]
    menus=list(menus)
    data=json.dumps(menus,ensure_ascii=False)
    return HttpResponse(data,'application/json')

@csrf_exempt
def strengthenlevel(request):
    mydata=zb_strengthen.objects.filter(level=1).values('sid','text')
    menus=[entry for entry in mydata]
    menus=list(menus)
    data=json.dumps(menus,ensure_ascii=False)
    return HttpResponse(data,'application/json')

