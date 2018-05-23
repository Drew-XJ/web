# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from .models import User,userInfo,resultInfo,version
from django.views.decorators import csrf
from datetime import datetime
from django import forms
from xlrd import xldate_as_tuple
import MySQLdb.cursors
import xlsxwriter
import xlrd
import time
import os

username_t = 'root'

def login(request):
    context = {"error":0}
    print request.method
    if request.method == "POST":
        input_name = request.POST[u'username']
        input_pwd = request.POST[u'password']
        result = User.objects.filter(username=input_name,password=input_pwd)    
        if(len(result)<=0):
            context['error'] = 1
            return render(request,'login.html',context)
        else:
            global username_t
            username_t = input_name
            context ["username"] = username_t
            return render(request,"login_succeed.html",context)
    return render(request,'login.html',context)

