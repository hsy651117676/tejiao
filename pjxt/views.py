from django.shortcuts import render
def indux(request):
    ctx ={}
    table_title=['YYY','XXX','PPP']
    ctx['dic']={"url":request,"name":"测试数据", "table_title":table_title}
    return render(request, "pjxt/base.html", ctx)

def echartstest(request):
    ctx ={}
    table_title=['YYY','XXX','PPP']
    ctx['dic']={"url":request,"name":"测试数据", "table_title":table_title}
    return render(request, "pjxt/echartstest.html", ctx)


