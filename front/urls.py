from django.urls import path
from front.views import index, futebol

urlpatterns = [
    path('', index, name='index'),
    path('futebol/', futebol, name='futebol')
]