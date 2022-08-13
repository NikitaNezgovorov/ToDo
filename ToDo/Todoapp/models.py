from django.db import models
from userapp.models import User


class Project(models.Model):
    name = models.CharField(max_length=64, unique=True)
    repository = models.URLField()
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class ToDo(models.Model):
    project_name = models.ForeignKey(Project, on_delete=models.CASCADE)
    text = models.TextField(max_length=255)
    create_date = models.DateTimeField(auto_now_add=1)
    update_date = models.DateTimeField(auto_now=1)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)
    is_active = models.BinaryField(default=True)
