from django.urls import path
from front.views import index, eventos, detalhes

urlpatterns = [
    path('', index, name='index'),
    path('eventos/', eventos, name='eventos'),
    path('detalhes/', detalhes, name='detalhes')
]