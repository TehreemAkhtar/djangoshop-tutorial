from django.urls import path

from store import views

urlpatterns = [
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:product_id>', views.ProductDetail.as_view(), name='product-detail'),
    path('collections/', views.CollectionList.as_view(), name='collection-list'),
    path('collections/<int:collection_id>', views.collection_detail, name='collection-detail'),
]