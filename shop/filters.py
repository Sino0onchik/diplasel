import django_filters
from .models import *


class CarFilter(django_filters.FilterSet):
    class Meta:
        model = Car
        ordering = ['-created_date']
        fields = ['category']
