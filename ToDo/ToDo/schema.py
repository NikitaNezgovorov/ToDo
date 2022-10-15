import graphene
from graphene import ObjectType, relay
from graphene_django import DjangoObjectType
from graphql.pyutils import description

import userapp
from Todoapp.models import ToDo, Project
from userapp.models import User


class ToDoType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = '__all__'


class ProjectUpdateMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        id = graphene.ID()

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, name, id):
        project = Project.objects.get(pk=id)
        project.name = name
        project.save()
        return ProjectUpdateMutation(project=project)


class ProjectCreateMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        users = graphene.List(graphene.ID, required=False)
        repository = graphene.String(required=False)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, users=None, **kwargs):
        project = Project.objects.create(**kwargs)

        if users is not None:
            users_set = []
            for user_id in users:
                users_objects = User.objects.get(pk=user_id)
                users_set.append(users_objects)
            project.users.set(users_set)
        project.save()


        return cls(project=project)


class ProjectDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.List(graphene.ID)
        # id = graphene.ID()
    projects = graphene.List(ProjectType)

    @classmethod
    def mutate(cls, root, info, id):
        for i in id:
            Project.objects.get(pk=i).delete()

        return cls(projects=Project.objects.all())


class Mutation(graphene.ObjectType):
    update_project = ProjectUpdateMutation.Field()
    create_project = ProjectCreateMutation.Field()
    delete_project = ProjectDeleteMutation.Field()


class Query(ObjectType):
    all_projects = graphene.List(ProjectType)
    all_todos = graphene.List(ToDoType)
    all_users = graphene.List(UserType)

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_todos(root, info):
        return ToDo.objects.all()

    def resolve_all_users(root, info):
        return User.objects.all()


schema = graphene.Schema(query=Query, mutation=Mutation)
