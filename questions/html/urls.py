from django.urls import path

from . import views
from . import admin  # needed for autodiscover

urlpatterns = [
    path('', views.index, name='index'),
]
