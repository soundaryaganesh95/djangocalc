from django.urls import path
from . import views

urlpatterns = [
    # Map the root of the calculator app to the calculator_view
    path('', views.calculator_view, name='calculator'),
]