from rest_framework_nested import routers

from store import views


router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')
router.register(r'collections', views.CollectionViewSet)
router.register(r'carts', views.CartViewSet, basename='carts')
router.register(r'customers', views.CustomerViewSet, basename='customers')
router.register(r'orders', views.OrderViewSet, basename='orders')

reviews_router = routers.NestedDefaultRouter(router, r'products', lookup='product')
reviews_router.register(r'reviews', views.ReviewViewSet, basename='product-reviews')

items_router = routers.NestedDefaultRouter(router, r'carts', lookup='cart')
items_router.register(r'items', views.CartItemViewSet, basename='cart-items')

images_router = routers.NestedDefaultRouter(router, r'products', lookup='product')
images_router.register(r'images', views.ProductImageViewSet, basename='product-images')

urlpatterns = router.urls + reviews_router.urls + items_router.urls + images_router.urls
