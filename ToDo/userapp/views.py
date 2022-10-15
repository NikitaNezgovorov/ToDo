# Create your views here.
from rest_framework import mixins, viewsets
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer

from .models import User
from .serializers import UserSerializer, UserSerializerWithIsStaffIsSuperuser


class UserViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, viewsets.GenericViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_serializer_class(self):
        if self.request.version == '1.0.0':
            return UserSerializerWithIsStaffIsSuperuser
        return UserSerializer
