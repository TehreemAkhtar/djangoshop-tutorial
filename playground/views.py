import requests
from django.shortcuts import render
from django.core.cache import cache
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
import logging


logger = logging.getLogger(__name__)


class HelloView(APIView):
    def get(self, request):
        try:
            logger.info("Calling httpbin")
            response = requests.get('https://httpbin.org/delay/2')
            logger.info("Received httpbin")
        except requests.ConnectionError:
            logger.critical("Connection error")
        return render(request, 'hello.html', context={'result': response.json()})


