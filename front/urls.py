from django.urls import path, include
from front.views import index, eventos, detalhes

urlpatterns = [
    path('', index, name='index'),
    path('eventos/', eventos, name='eventos'),
    path('detalhes/', detalhes, name='detalhes'),
    path('accounts/', include('allauth.urls')),
]