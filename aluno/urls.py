from django.urls import path
from aluno.views import index

urlpatterns = [
    path('', index, name='home'),
]
