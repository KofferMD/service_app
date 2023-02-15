from rest_framework.serializers import ModelSerializer

from booking.models import Cat


class CatsSerializer(ModelSerializer):
    class Meta:
        model = Cat
        fields = ('__all__')

