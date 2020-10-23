from django.shortcuts import render
from django.http import HttpResponseRedirect

from .models import Product

from .forms import ProductForm, RawProductForm
# Create your views here.

def product_create_view(request):

    myform = RawProductForm()
    if request.method == 'POST':
        myform = RawProductForm(request.POST)
        if myform.is_valid():
            print(myform.cleaned_data)
            Product.objects.create(**myform.cleaned_data)
        else:
            print(myform.errors)
    context={
      'form': myform
    }
    return render(request, "product/create.html",context)
# def product_create_view(request):
#     print(request.GET['title'])
#     print(request.POST)
#     title = request.POST.get
#     ('title')
#     print(title)
#     context={
      
#     }
#     return render(request, "product/create.html",context)

#def product_create_view(request):
#    form = ProductForm(request.POST or None)

 #   if form.is_valid():
 #       form.save()
 #       form = ProductForm()
 #   context={
 #       'form': form
 #   }
 #   return render(request, "product/create.html",context)



def product_detail_view(request):
    obj=Product.objects.get(id=1)
    ##context={'title':obj.title,
    ##'description':obj.description
    ##}
    context={
        'object': obj
    }
    return render(request, "product/detail.html",context)