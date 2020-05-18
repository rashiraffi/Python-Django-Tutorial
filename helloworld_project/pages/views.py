from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

"""
Basically we’re saying whenever the view function homePageView is called, return
the text “Hello, World!” More specifically, we’ve imported the built-in HttpResponse
method so we can return a response object to the user. We’ve created a function called 
homePageView that accepts the request object and returns a response with the string
Hello, World! .
"""


def homePageView(request):
    return HttpResponse('Hello, World')