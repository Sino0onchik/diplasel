from django.shortcuts import render, redirect
from django.views import generic

from .forms import OrderForm
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
        if self.request.GET.get('category'):
            context['category'] = Category.objects.get(id=self.request.GET.get('category'))
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


class OrderCreateView(generic.CreateView):
    template_name = 'basket.html'
    model = Order
    queryset = Order.objects.all()
    form_class = OrderForm
    context_object_name = 'form'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.car = Car.objects.get(id=kwargs.get('pk'))
            order.save()
        print(form.errors)
        return redirect('/')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context
