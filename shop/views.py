from django.shortcuts import render
from django.views import generic
from .models import *
from .filters import CarFilter


class HomeView(generic.ListView):
    template_name = 'index.html'
    model = Car
    filter_class = CarFilter
    paginate_by = 10
    context_object_name = 'cars'
    queryset = Car.objects.all()

    def get_queryset(self):
        query = Car.objects.all()
        filter = CarFilter(self.request.GET, queryset=query)
        query = filter.qs
        return query

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['companies'] = Company.objects.all()
        return context


class CarDetailView(generic.DetailView):
    template_name = 'itemDetail.html'
    queryset = Car.objects.all()
    model = Car

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['another_cars'] = Car.objects.all().order_by('?')[:8]
        context['categories'] = Category.objects.all()
        return context


class CompanyDetailView(generic.DetailView):
    template_name = 'detail.html'
    queryset = Company.objects.all()
    model = Company

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
