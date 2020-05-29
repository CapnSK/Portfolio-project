from django.http import HttpResponse
from django.shortcuts import render

def acting(request):
	return render(request,'acting.html')

def weightLifting(request):
	return render(request,'weightlifting.html')