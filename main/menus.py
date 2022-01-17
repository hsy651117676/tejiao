import os
import json,requests
from django.shortcuts import render,HttpResponse,redirect
from django.contrib import auth
from django.views.decorators import csrf
from django.contrib.auth import  login
from django.contrib.auth.models import User,Group 
from main.models import * 

def main_menu(user):
    menus=menutree('10') # 每个用户都要显示的菜单
    menus=menus + menutree('11') # 每个用户都要显示的菜单
    if user.groups.filter(name='系统管理员组').exists():
        menus=menus + menutree('01')
    if user.groups.filter(name='学校领导组').exists():
        menus=menus + menutree('02')
    if user.groups.filter(name='教师组').exists():
        menus=menus + menutree('03')
    return menus

def menutree(mpid):
    div1=menu.objects.filter(level=1,pid=mpid)
    menuhtml=''
    for var in div1:
        level2=''
        btn=menu.objects.filter(level=2,pid=var.mid)
        for a in btn:
            abtn='<' + a.melement + ' href="' + a.mhref + '" src="' + a.msrc + '" class="' + a.mclass + '" data-options="' + a.mdataoption + '" >' + a.mtitle + '</' + a.melement + '>'
            level2=level2 + abtn
        level1='<' + var.melement + ' title="'+ var.mtitle + '" data-options="'+ var.mdataoption + '" style="'+ var.mstyle + '">' + level2 + '</' + var.melement + '>'
        menuhtml=menuhtml+ level1
    return menuhtml

 


