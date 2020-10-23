from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request, *args, **kwargs):
    print(args,kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello world</h1>")
    return render(request,'home.html',{})

def contact_view(request, *args, **kwargs):
	
    return render(request,'contact.html',{})
def kak_view(request, *args, **kwargs):
    my_context={"my_text":"o tebe",
    "my_heart":"O nas",
    "my_age":12,
    "my_list":[123,232,444,"Abc"],
    "my_html":"<h1>My contents!!@</h1>"
    }

    return render(request,'kak.html',my_context)

def katamaran_view(request, *args, **kwargs):
	return render(request,'katamaran.html',{})
