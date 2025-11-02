from django.shortcuts import render

# Create your views here.
from properties.models import Property
from properties.serializers import PropertySerializer
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from .utils import get_all_properties
# Create your views here.


@api_view(["GET"])
#@cache_page(60 * 15)
def property_list(request):
  data = get_all_properties()
  return data
  
