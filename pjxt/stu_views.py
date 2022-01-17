from django.shortcuts import render
import json,requests
from pjxt.models import *
from main import mytools

def Fstu(request):
    ctx ={}
    ctx['dic']={"url":request,"name":"测试数据"}
    return render(request, "pjxt/stu/manage.html", ctx)

def Fstu_edit(request):
    stuid=request.GET['id']
    name=request.GET['name']
    #对学生标识stuid和学生相关的几张表名称进行加密并放入列表中的字典, 为下一步Fstu_update函数更新学生表做准备。
    tablename=['stu_info','stu_ifamily','stu_enrol','stu_viability','stu_vstrengthen']
    # 注意此处的列表tablename与模板文件edit.html顺序一一对应！
    newstr=[]
    for i in tablename:
        # i指 strid,t指tablename
        oldstr="{'i':'" + stuid + "','u':'" + i + "'}"
        jm=mytools.AEScoder()
        aes=jm.encrypt(oldstr)
        newstr.append(aes)
    ctx ={}
    ctx['dic']={"url":request,"id":newstr,"name":name}
    return render(request, "pjxt/stu/edit.html", ctx)

def Fstu_update(request):
    pid=request.GET['id']
    pname=request.GET['name']
    e=1 
    ctx ={}
    ctx['dic']={"url":request,"id":e}
    return render(request, "pjxt/stu/edit.html", ctx)

def Fstu_enrol(request):
    pid=request.GET['id']
    jm=mytools.AEScoder()
    pid=jm.encrypt(pid)
    dic=eval(pid)
    pid=dic['i']
    mydata=stu_enrol.objects.filter(stuid=pid).values()
    menus=[entry for entry in mydata]
    menus=list(menus)
    data=json.dumps(menus,ensure_ascii=False)
    ctx ={}
    ctx['dic']={"data":data}
    return render(request, "pjxt/base.html", ctx)

def Fstu_family(request):
    pid=request.GET['id']
    jm=mytools.AEScoder()
    pid=jm.encrypt(pid)
    dic=eval(pid)
    pid=dic['i']
    mydata=stu_family.objects.filter(stuid=pid).values()
    menus=[entry for entry in mydata]
    menus=list(menus)
    data=json.dumps(menus,ensure_ascii=False)
    ctx ={}
    ctx['dic']={"data":data}
    return render(request, "pjxt/base.html", ctx)

def Fstu_info(request):
    pid=request.GET['id']
    print(pid[2:66])
    jm=mytools.AEScoder()
    pid=jm.decrypt(pid[2:66])
    pid=1
    mydata=stu_info.objects.filter(stuid=pid).values()
    menus=[entry for entry in mydata]
    menus=list(menus)
    data=json.dumps(menus,ensure_ascii=False)
    ctx ={}
    ctx['dic']={"data":data}
    return render(request, "pjxt/base.html", ctx)

def Fstu_viability(request):
    pid=request.GET['id']
    jm=mytools.AEScoder()
    pid=jm.encrypt(pid)
    dic=eval(pid)
    pid=dic['i']
    mydata=stu_viability.objects.filter(stuid=pid).values()
    menus=[entry for entry in mydata]
    menus=list(menus)
    data=json.dumps(menus,ensure_ascii=False)
    ctx ={}
    ctx['dic']={"data":data}
    return render(request, "pjxt/base.html", ctx)

def Fstu_strengthen(request):
    pid=request.GET['id']
    jm=mytools.AEScoder()
    pid=jm.encrypt(pid)
    dic=eval(pid)
    pid=dic['i']
    mydata=stu_strengthen.objects.filter(stuid=pid).values()
    menus=[entry for entry in mydata]
    menus=list(menus)
    data=json.dumps(menus,ensure_ascii=False)
    ctx ={}
    ctx['dic']={"data":data}
    return render(request, "pjxt/base.html", ctx)


