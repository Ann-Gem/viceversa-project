from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, "home.html")

count = 0
def reverse(request):

	user_text = request.GET['usertext']
	n = user_text.count(' ') + 1
	reversed_text = user_text[::-1]
	return render(request, 'reverse.html' , {'usertext':user_text, 'reversedtext': reversed_text, 'number_of_words':n})