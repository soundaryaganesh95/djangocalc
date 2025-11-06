# ECOMMERCE/ECOMMERCE/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # The calculator app is mapped to '/calc/'
    # ECOMMERCE/ECOMMERCE/urls.py
path('calc/', include('calculator.urls')),
]