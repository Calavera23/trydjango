from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello world</h1>")
    return render(request,'home.html',{})

def contact_view(request, *args, **kwargs):
	
    return HttpResponse("<h1>Contact page</h1>")
def kak_view(request, *args, **kwargs):
    return HttpResponse("<h1>Kak</h1>")

def katamaran_view(request, *args, **kwargs):
	return HttpResponse("<h1>Katamaran page</h1>")
