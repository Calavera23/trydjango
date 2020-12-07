from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ProductForm, RawProductForm
from .models import Product

# Create your views here.

# def product_create_view(request):
#     print(request.GET['title'])
#     print(request.POST)
#     title = request.POST.get
#     ('title')
#     print(title)
#     context={
      
#     }
#     return render(request, "product/create.html",context)

def product_create_view(request):
   form = ProductForm(request.POST or None)

   if form.is_valid():
       form.save()
       print("form saved")
       form = ProductForm()
   context={
       'form': form
   }
   return render(request, "product/create.html",context)



def product_detail_view(request):
    obj=Product.objects.get(id=1)
    ##context={'title':obj.title,
    ##'description':obj.description
    ##}
    context={
        'object': obj
    }
    return render(request, "product/detail.html",context)


def render_initial_data(request):
    initial_data = {
        'title':"This is title!"
    }
    obj=Product.objects.get(id=1)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context={
        'form': form
        
    }
    return render(request,"product/create.html",context)

def dynamic_lookup_view(request, myid):
   # obj = Product.objects.get(id=myid)
    #obj=get_object_or_404(Product, id=myid)
    obj=Product.objects.get(id=myid)
    #try:
    #    obj=Product.objects.get(id=myid)
    #except Product.DoesNotExist:
    #        raise Http404
    context={
         "object": obj
        }
    return render(request,"product/detail.html", context)

def product_delete_view(request, myid):
    obj=get_object_or_404(Product, id=myid)
    if request.method == 'POST':
        obj.delete()
        return HttpResponseRedirect('/product/list/')
    context={
         "object": obj
    }
    return render(request,"product/delete.html", context)

def product_list_view(request):
    
    queryset = Product.objects.all()
    context = {
        "object_list": queryset
    }

    return render(request, "product/list.html", context)