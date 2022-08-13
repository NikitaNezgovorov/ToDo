from django_filters import rest_framework as filters
from .models import ToDo


class ToDoFilter(filters.FilterSet):
    create_date = filters.DateFromToRangeFilter()

    class Meta:
        model = ToDo
        fields = ['project_name', 'create_date']
