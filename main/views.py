import os
from django.shortcuts import render,HttpResponse,redirect
from django.views.decorators import csrf
from django.contrib import auth
from django.contrib.auth import authenticate, login
from . import menus 

def index_view(request):
    status = request.COOKIES.get('is_login') # 收到浏览器的再次请求,判断浏览器携带的cookie是不是登录成功的时候响应的 cookie
    if not status:
         return redirect("/login/") 
    if not request.user.is_authenticated:
        return redirect("/login/")
    #登录成功执行
    ctx ={}
    menu=menus.main_menu(request.user)
    ctx['dic']={"menu":menu}
    return render(request, "index.html", ctx)

def login_view(request):
    if request.method == "GET":
        return render(request, "login.html")
    username = request.POST.get("username")
    password = request.POST.get("pswd")
    user= authenticate(username=username,password=password)
    if user:
        auth.login(request,user)
        rep = redirect("/index/")
        rep.set_signed_cookie("is_login",user,salt='is_login_jmy',max_age=60*30)
        rep.user=user
        return rep
    else:
        return redirect("/login/")

def logout_view(request):
    auth.logout(request)
    rep = redirect('/login/')
    rep.delete_cookie("is_login")
    request.session.flush()
    return rep # 点击注销后执行,删除cookie,不再保存用户状态，并弹到登录页面
   
def order(request):
    status = request.COOKIES.get('is_login')
    if not status:
        return redirect('/login/')
    return render(request, "order.html")

def page_not_found(request,exception):
    return render(request, '404.html')

def page_error(request):
    return render(request, '500.html')

def permission_denied(request,exception):
    return render(request, '403.html')
