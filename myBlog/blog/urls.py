from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('counter', views.counter, name='counter')  #action = "{% url 'counter' %}" in index.html
]