from rest_framework import serializers
from .models import *

class ArtistsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artists
        fields = ['artistID', 'first_name', 'last_name']