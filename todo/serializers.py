from rest_framework import serializers
from .models import ToDo

class ToDoSerializer(serializers.ModelSerializer):


    class Meta:
        model = ToDo
        fields = ['id', 'user', 'task', 'completed', 'created_at']
