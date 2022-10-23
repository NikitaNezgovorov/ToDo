from rest_framework.serializers import ModelSerializer

from userapp.serializers import UserSerializer
from .models import Project, ToDo


class ProjectSerializer(ModelSerializer):
    # owner = HyperlinkedIdentityField(view_name='user-detail')
    # users = UserSerializer(many=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'users', 'repository']


class ToDoSerializer(ModelSerializer):
    # project_name = HyperlinkedIdentityField(view_name='project-detail')
    # creator = HyperlinkedIdentityField(view_name='user-detail')

    class Meta:
        model = ToDo
        fields = ['id', 'project_name', 'text', 'create_date', 'update_date', 'creator']
