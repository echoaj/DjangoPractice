from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse('<h1>Home Page</h1>')
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    #return HttpResponse('<h1>Contact Page</h1>')
    return render(request, "contact.html", {'info':['ajosiln@gmail.com', '(123) 456-7389', 'linkedin/aj']})

def about_view(request, *args, **kwargs):
    #return HttpResponse('<h1>About Page</h1>')
    return render(request, "about.html", {'title':'The About'})