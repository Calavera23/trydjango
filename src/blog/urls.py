from django.urls import path
from .views import (
    ArticleListView,
    ArticleCreateView,
    ArticleDetailView,
    ArticleUpdateView,
    ArticleDeleteView
)

app_name='articles'
urlpatterns=[
    path('',ArticleListView.as_view(template_name = 'blog/article_list.html')),

    path('<int:pk>/',ArticleDetailView.as_view(template_name = 'blog/article_detail.html'),name='article'),
    path('<int:pk>/update/',ArticleUpdateView.as_view(template_name = 'blog/article_update.html'),name='article-update'),
    path('<int:pk>/delete/',ArticleDeleteView.as_view(template_name = 'blog/article_delete.html'),name='article-delete'),

    path('create', ArticleCreateView.as_view(template_name = 'blog/article_create.html'), name='article-add'),
]