from rest_framework import serializers
from .models import Task_List

class taskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task_List
        fields = '__all__'
        
class task2Serializer(serializers.ModelSerializer):
    class Meta:
        model = Task_List
        fields = '__all__'
