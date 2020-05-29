from django.shortcuts import render
from .models import Achievment

def coding(request):
	a=Achievment.objects
	achievmentDict = {}
	for achievment in a.all():
		achievmentDict[achievment.id]={'title':achievment.title,'summary':achievment.summary}
	return render(request,'achievments/coding.html',{'achievmentDict':sorted(achievmentDict.items())})