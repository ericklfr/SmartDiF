from rest_framework.serializers import ModelSerializer
from api.models import SomarAPI


class SomarAPISerializer(ModelSerializer):

    class Meta:
        model = SomarAPI
        fields = '__all__'
