"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from . import views,zb_views,stu_views
from django.urls import path,include,re_path

urlpatterns = [
        path('gradeinfo/',views.indux),
        path('classinfo/',views.indux),
        path('studentinfo/',views.indux),
        path('teacherinfo/',views.indux),
        path('qhwdcb/',views.indux),
        path('xqztghb/',views.echartstest),
        
        path('stu/',stu_views.Fstu),
        path('stu/edit',stu_views.Fstu_edit),
        path('stu/update',stu_views.Fstu_update),
        path('stu/info/',stu_views.Fstu_info),
        path('stu/enrol/',stu_views.Fstu_enrol),
        path('stu/family/',stu_views.Fstu_family),
        path('stu/viability/',stu_views.Fstu_viability),
        path('stu/strengthen/',stu_views.Fstu_strengthen),
        
        path('zb_viability/',zb_views.Fzb_viability),
        path('zb_viability/level',zb_views.viabilitylevel),
        path('zb_viability/update',zb_views.viabilityupdate),
        path('zb_viability/ajax',zb_views.viabilityajax),

        path('zb_strengthen/',zb_views.Fzb_strengthen),
        path('zb_strengthen/level',zb_views.strengthenlevel),
        path('zb_strengthen/update',zb_views.strengthenupdate),
        path('zb_strengthen/ajax',zb_views.strengthenajax),
      ]

