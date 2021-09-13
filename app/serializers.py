from rest_framework import serializers
from .models import Emp

class EmpSerializer(serializers.Serializer):
    class Meta:
        model = Emp
        fields = '__all__'
    # def create(self, validated_data):
    #     return EmpSerializer()
    #     EmpSerializer.save()

