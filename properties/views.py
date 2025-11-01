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
# Create your views here.


@api_view(["GET"])
@cache_page(60 * 15)
def property_list(request):
  property = Property.objects.all()
  serialized = PropertySerializer(property, many=True)
  return JsonResponse(serialized.data, safe=False)
