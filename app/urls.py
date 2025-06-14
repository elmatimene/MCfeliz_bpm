from django.urls import path
from .views import home, agendar

urlpatterns = [
    path('',home, name='home'),
    path('agendar/',agendar, name='agendar'),
]