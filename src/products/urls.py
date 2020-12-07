from django.urls import path
from .views import(
    product_create_view, product_delete_view,product_detail_view,render_initial_data, dynamic_lookup_view,
    product_list_view
)
app_name='products'
urlpatterns = [
    path('initial/',render_initial_data ),
    path('<int:myid>/',dynamic_lookup_view, name='product'),
    path('<int:myid>/delete', product_delete_view, name='product-delete'),
    path('create/',product_create_view ),
    path('list/', product_list_view),
]