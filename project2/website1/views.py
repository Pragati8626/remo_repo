from django.shortcuts import render
from django.http import HttpResponse
def fun1(request):
	return HttpResponse("Good morning")

def fun2(request):
	return HttpResponse("Good afternoon")
# Create your views here.
