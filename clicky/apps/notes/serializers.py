from rest_framework import serializers
from .models import Note


class NoteSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(
        format="%Y-%m-%d %H:%M", read_only=True
    )

    class Meta:
        model = Note
        fields = '__all__'
