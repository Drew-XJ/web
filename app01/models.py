# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class userInfo(models.Model):
    name = models.CharField(max_length=50)
    dname = models.CharField(max_length=20)
    sex = models.CharField(max_length = 2)
    tel = models.CharField(max_length=15)
    money = models.IntegerField()
    deadline = models.CharField(max_length=15)
    delay = models.IntegerField()
    utype = models.IntegerField()
    importdate = models.CharField(max_length=15)
    flag = models.IntegerField()

class resultInfo(models.Model):
    name = models.CharField(max_length=50)
    dname = models.CharField(max_length=20)
    tel = models.CharField(max_length=15)
    contactdate = models.CharField(max_length=15)
    contactstatus = models.CharField(max_length=20)
    casestatus = models.CharField(max_length=10)
    expectdate = models.CharField(max_length=15)

class version(models.Model):
    versions =  models.CharField(max_length = 20)