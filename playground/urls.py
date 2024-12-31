from django.urls import path
from playground import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
]
