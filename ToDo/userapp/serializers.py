from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from .models import User


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
