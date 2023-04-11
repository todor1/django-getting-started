from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def welcome(request):
    # return render(request, "website/welcome.html")
    return render(request, "website/welcome.html",
                  {'message': 'My message created from the Views welcome function.'})

# def welcome(request):
#     return HttpResponse("Welcome to the Meeting Planner!")

def date(request):
    return HttpResponse(f'This page was served at {datetime.now():%Y-%m-%d %H:%M:%S}')

def about(request):
    '''Multiple line strings displayed as a single line in HTML on page'''
    
    msg_about = f'''Hello and welcome to my page.\n
                Glad to meet you here at {datetime.now():%Y-%m-%d %H:%M:%S}\n
                Please check out my other pages.\n
                '''
    return HttpResponse(msg_about)

