from rest_framework import serializers

class PropertySerializer(serializers.ModelSerializer):
  class Meta:
    model = property
    fields = "__all__"