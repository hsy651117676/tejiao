import os
import json,requests
from django.views.decorators import csrf
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import auth
from django.http import JsonResponse
from django.core import serializers
from . import menus
from main.models import *
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect
from django.conf import settings


def menuedit(request):
    data=[]
    ctx ={}
    title=['YYY','XXX','PPP']
    ctx['dic']={'table_title':title,'data':data}
    return render(request, "main/sysmenuedit.html", ctx)

@csrf_exempt
def menuupdate(request):
    data=json.loads(request.body)
    for i in data:
        if "id" in i:
            menu.objects.filter(id=i['id']).update(**i)
        else:
            del i['row']
            menu.objects.create(**i)
    return HttpResponse('200','application/json')

@csrf_exempt
def menuajax(request):
    pa1=request.POST['PA1']
    mydata=menu.objects.filter(mid__startswith=pa1).values().order_by("level","pid")
    menus=[entry for entry in mydata]
    menus=list(menus)
    data=json.dumps(menus,ensure_ascii=False)
    return HttpResponse(data,'application/json')

@csrf_exempt
def menulevel(request):
    mydata=menu.objects.filter(level=1).values('mid','mtitle')
    menus=[entry for entry in mydata]
    menus=list(menus)
    data=json.dumps(menus,ensure_ascii=False)
    return HttpResponse(data,'application/json')

def usermanage(request):
    ctx ={}
    table_title=['YYY','XXX','PPP']
    ctx['dic']={"url":request,"name":"测试数据", "table_title":table_title}
    return render(request, "main/sysmenuedit.html", ctx)

class LoginRequiredMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.login_url = settings.LOGIN_URL
        self.open_urls = [self.login_url] + getattr(settings, 'OPEN_URLS', [])
    def __call__(self, request):
        if not request.user.is_authenticated and request.path_info not in self.open_urls:
            return redirect(self.login_url + '?next=' + request.path)
        return self.get_response(request)
