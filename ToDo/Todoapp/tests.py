import json

from django.test import TestCase
# Create your tests here.
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APITestCase, force_authenticate

from .models import ToDo, Project
from .views import ProjectViewSet, ToDoViewSet
from userapp.models import User


class TestProjectViewSet(TestCase):

    def setUp(self):
        self.url = '/api/projects/'
        self.project_dict = {"name": "Nick", "repository": "https://docs.djangoproject.com", "users": [1]}
        self.project_dict_fake = {"name": "Nick!!!", "repository": "https://docs.m", "users": [2]}
        self.format = 'json'
        self.login = 'Nick'
        self.password = '1'
        # self.admin = User.objects.create_superuser(self.login, 'admin@mail.ru', self.password)

    def test_factory_get_list(self):
        factory = APIRequestFactory()
        request = factory.get(self.url)
        view = ProjectViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_factory_create(self):
        factory = APIRequestFactory()
        request = factory.post(self.url)
        view = ProjectViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TestTodoViewSet(APITestCase):

    def setUp(self):
        self.url = '/api/todos/'
        self.factory = APIRequestFactory()
        self.login = 'Nick'
        self.password = '1'
        self.format = 'json'
        self.user = User.objects.create()
        self.project = Project.objects.create(name='project1', repository='')
        self.admin = User.objects.create_superuser(self.login, 'admin@mail.ru', self.password)
        self.data = {'project_name': self.project, 'text': 'subject1', 'creator': self.admin}
        self.data_post = {'project_name': self.project.id, 'text': 'subject1', 'creator': self.admin.id}

    def test_get_list_testcase(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_guest(self):
        request = self.factory.post(self.url, self.data_post, format=self.format)
        view = ToDoViewSet.as_view({'post': 'create'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_admin(self):
        request = self.factory.post(self.url, self.data_post, format=self.format)
        force_authenticate(request, self.admin)

        view = ToDoViewSet.as_view({'post': 'create'})
        response = view(request)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_edit_admin_apiclient(self):
        todo = ToDo.objects.create(**self.data)
        new_text = 'text new'
        new_data = json.dumps({'project_name': self.project.id, 'creator': self.admin.id, 'text': new_text})

        self.client.login(username=self.admin.username, password=self.password)

        response = self.client.put(f'{self.url}{todo.id}/', new_data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        todo.refresh_from_db()

        self.assertEqual(todo.text, new_text)

        self.client.logout()

    def tearDown(self) -> None:
        pass
