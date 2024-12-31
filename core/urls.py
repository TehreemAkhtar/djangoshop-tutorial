from django.urls import path
from django.views.generic import TemplateView

from playground import views

urlpatterns = [
    path('', TemplateView.as_view(template_name='core/index.html'), name='hello'),
]
