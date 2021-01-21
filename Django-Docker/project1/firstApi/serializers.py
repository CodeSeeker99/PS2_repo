from rest_framework import serializers
from firstApi.models import PytorchModel

class PytorchModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PytorchModel
        fields = ('id', 'name', 'desc', 'last_updated')