

from django.http import HttpResponse

from django.shortcuts import render
def Hello(request):
    return HttpResponse("Hello")
def World(request):
    return HttpResponse("World")
def Welcome(request):
    context = {'tag_var':"tag_var"}
    return render(request,"app1/demo.html",context)


