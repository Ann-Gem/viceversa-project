from django.http import HttpResponse
from django.shortcuts import render



def viceversa(request):
	return render(request, 'home.html')

def textarea(request):
	return render(request, 'home.html')

def button(request):
    return render(request, "home.html")


