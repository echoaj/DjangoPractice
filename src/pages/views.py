from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    print("----------")
    print(args)
    print(kwargs)
    print(request)
    print("----------")
    return HttpResponse('<h1>Home Page</h1>')

def contact_view(*args, **kwargs):
    return HttpResponse('<h1>Contact Page</h1>')

def about_view(*args, **kwargs):
    return HttpResponse('<h1>About Page</h1>')