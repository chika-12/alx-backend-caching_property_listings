import os
from dotenv import load_dotenv
from django.core.exceptions import ImproperlyConfigured
from django.core.cache import cache
from django.http import JsonResponse
from rest_framework.response import Response
load_dotenv()

# def verify_os_variables(var_name):
#   variable = os.getenv(var_name)
#   if variable is None:
#     raise ImproperlyConfigured(f"{var_name} cant be found")
#   return variable

def get_all_properties():
  from .models import Property
  from .serializers import PropertySerializer
  cached_properties = cache.get('property_list')

  if cached_properties:
    return Response({"data": cached_properties, "cached": True})
  
  properties = Property.objects.all()
  serialized = PropertySerializer(properties, many=True).data
  cache.set('property_list', serialized, 3600)
  return Response({'data': serialized, 'cached': False})

