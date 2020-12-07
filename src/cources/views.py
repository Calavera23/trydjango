from django.shortcuts import render, get_object_or_404,redirect
from django.views import View

from .models import Cource
from .forms import CourceModelForm
from django.shortcuts import render, get_object_or_404, redirect
class CourceObjectMixin(object):
	model=Cource
	url_lookup='id'
	def get_object(self):
		id = self.kwargs.get(self.url_lookup)
		obj = None
		if id is not None:
			obj=get_object_or_404(self.model, id=id)
		return obj



class CourceCreateView(View):
	template_name = 'cources/create.html'
	"""docstring for ClassName"""
	def get(self, request, *args,**kwargs):
		form=CourceModelForm()
		context={"form":form}
		return render(request,self.template_name,context)

	def post(self, request, *args,**kwargs):
		form=CourceModelForm(request.POST)
		if form.is_valid():
			form.save()
			form=CourceModelForm()

		context={"form":form}
		return render(request,self.template_name,context)

class CourceUpdateView(CourceObjectMixin,View):
	template_name = 'cources/create.html'


	def get(self, request, id=None ,*args,**kwargs):
		context={}
		obj=self.get_object()
		if obj is not None:

			form=CourceModelForm(instance=obj)

			context={"form":form, "object":obj}
		return render(request,self.template_name,context)

	def post(self, request, id=None,*args,**kwargs):
		context={}
		obj=self.get_object()
		if obj is not None:
			form=CourceModelForm(request.POST,instance=obj)
			if form.is_valid():
				form.save()
			context={"form":form,"object":obj}
		return render(request,self.template_name,context)

class CourceDeleteView(CourceObjectMixin,View):
	template_name = 'cources/delete.html'

	def get(self, request, id=None ,*args,**kwargs):
		context={}
		obj=self.get_object()
		if obj is not None:

			form=CourceModelForm(instance=obj)

			context={"form":form, "object":obj}
		return render(request,self.template_name,context)

	def post(self, request, id=None,*args,**kwargs):
		context={}
		obj=self.get_object()
		if obj is not None:
			
			obj.delete()
			context={"object":None}
			return redirect('/cources/')
		return render(request,self.template_name,context)

class CourceListView(View):
	template_name="cources/list.html"
	queryset=Cource.objects.all()

	def get_queryset(self):
		return self.queryset

	def get(self, request, *args,**kwargs):
		context={'object_list': self.queryset}
		queryset=Cource.objects.all()

		return render(request,self.template_name, context)



class CourceView(CourceObjectMixin, View):
	template_name = 'cources/detail.html'
	"""docstring for ClassName"""
	def get(self, request, id=None, *args,**kwargs):
		context={"object":self.get_object()}

		return render(request,self.template_name,context)
# Create your views here.
def my_fbv(request, *args,**kwargs):
	return render(request,self.template_name,{})