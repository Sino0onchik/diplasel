from django.urls import path
from .views import *


urlpatterns = [
    path('', HomeView.as_view()),
    path('car/detail/<int:pk>/', CarDetailView.as_view()),
    path('company/detail/<int:pk>/', CompanyDetailView.as_view()),
    path('order/create/<int:pk>/', OrderCreateView.as_view()),
]
