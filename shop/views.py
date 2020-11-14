from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return render(request, 'shop/index.html')


def about(request):
    return render(request, 'shop/about.html')


def contact(request):
    return HttpResponse('This is contact')


def tracker(request):
    return HttpResponse('This is tracker')


def search(request):
    return HttpResponse('This is search')


def productView(request):
    return HttpResponse('This is product view')


def checkout(request):
    return HttpResponse('This is checkout')
