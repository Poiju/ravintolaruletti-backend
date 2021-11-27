from django.db.models import fields
from rest_framework import serializers
from ravintolat.models import Ravintola

class RavintolaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ravintola
        fields = ['name', 'photoURL']

