# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


def index(request):
    response = "hello i am response"
    return HttpResponse(response)

# Create your views here.
