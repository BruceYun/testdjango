# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
from django.shortcuts import  render_to_response

def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        return HttpResponse('1231231231')
    else:
        return render_to_response('login.html')