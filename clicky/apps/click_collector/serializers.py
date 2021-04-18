from rest_framework import serializers
from .models import Click


class ClickSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S.%f")

    class Meta:
        model = Click
        fields = '__all__'
