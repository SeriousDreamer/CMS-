from django.shortcuts import render
from django.http import HttpResponse
from . import add_manager


# Create your views here.
def add(request):
    add_manager.add('root', 1996010207)
    return HttpResponse(r'添加成功')
