from django.urls import path
from .views import (
    my_fbv,
    CourceView,
    CourceListView,
    CourceCreateView,CourceUpdateView,CourceDeleteView
)

app_name='cources'
urlpatterns=[
   # path('',my_fbv,name='cources-list'),
   # path('contact/',my_fbv,name='cources-list'),

    path('',CourceListView.as_view(),name='cources-list'),

    path('<int:id>/',CourceView.as_view(),name='cource'),
    
    path('<int:id>/update/',CourceUpdateView.as_view(),name='cource-update'),
    path('<int:id>/delete/',CourceDeleteView.as_view(),name='cource-delete'),

    path('create/', CourceCreateView.as_view(template_name = 'cources/create.html')),
]