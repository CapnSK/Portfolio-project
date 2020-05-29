from django.shortcuts import render
from .models import Job
from django.urls import reverse

def home(request):
	jobs = Job.objects
	jobDict = {}
	for job in jobs.all():
		if '/' not in job.uri:
			jobDict[job.id]={'title':job.title,'image':job.image,'summary':job.summary,'uri':reverse(job.uri)}
		else:
			jobDict[job.id]={'title':job.title,'image':job.image,'summary':job.summary,'uri':job.uri}
	return render(request,'jobs/home.html', {'jobDict':sorted(jobDict.items())})