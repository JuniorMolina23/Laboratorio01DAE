from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('suma/<int:n1>/<int:n2>', views.suma, name='suma'),
    path('resta/<int:n1>/<int:n2>', views.resta, name='resta'),
    path('mult/<int:n1>/<int:n2>', views.mul, name='mul'),
    path('div/<int:n1>/<int:n2>', views.div, name='div'),
]