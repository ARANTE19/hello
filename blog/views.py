from django.shortcuts import render
from django.http import HttpResponse
from blog.models import todo
# Create your views here.

def index(request):
    ret={}
    ret['name']=request.GET.get('name')
    #ret['length']=range(len(ret['name']))
    print ret
    print request.GET
    return render(request,'login.html',ret)
def list_todo(request):
    ret={}
    ret['todo']=todo.Object.all()
    return render(request,'todo.html',ret)
    