from django.shortcuts import render
from properties.models import Property
from properties.serializers import PropertySerializer
from django.views.decorators.cache import cache_page
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .utils import get_all_properties
from django.core.cache import cache

# Create your views here.


@api_view(["GET", "POST"])
#@cache_page(60 * 15)
def property_list(request):
  if request.method == "GET":
    # properties = Property.objects.all()
    # serialized = PropertySerializer(properties, many=True)
    # return Response(serialized.data, status=status.HTTP_200_OK)
    data = get_all_properties()
    return data
  
  if request.method == "POST":
    serialize = PropertySerializer(data=request.data, many=isinstance(request.data, list))
    if serialize.is_valid():
      serialize.save()
      #cache.delete('property_list')
      return Response(serialize.data, status=status.HTTP_201_CREATED)
    else:
      return Response(serialize.errors, status=status.HTTP_400_BAD_REQUEST)
    




