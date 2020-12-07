
from django.http import HttpResponse
from django.views.generic import(
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleModelForm
# Create your views here.
class ArticleListView(ListView):
    queryset=Article.objects.all()

class ArticleDetailView(DetailView):
    template_name='blog/article_detail.html'
    queryset=Article.objects.all()

    def get_object(self):
        id_=self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)

class ArticleDeleteView(DeleteView):
    template_name='blog/article_delete.html'
    queryset=Article.objects.all()

    def get_success_url(self):
        return "../../"

    def get_object(self):
        id_=self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)

class ArticleCreateView(CreateView):
    form_class=ArticleModelForm
    model=Article
    queryset=Article.objects.all()

    def form_valid(self, form):
        print("form saved")
        return super().form_valid(form)
    def get_success_url(self):
        return "."

class ArticleUpdateView(UpdateView):
    form_class=ArticleModelForm
    model=Article
    queryset=Article.objects.all()

    def get_object(self):
        id_=self.kwargs.get("pk")
        return get_object_or_404(Article, id=id_)
        
    def form_valid(self, form):
        print("form saved")
        return super().form_valid(form)

