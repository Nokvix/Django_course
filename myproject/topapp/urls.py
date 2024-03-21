from django.urls import path
from . import views

urlpatterns = [
    path('', views.fullname, name='index'),
    path('poem/', views.poem, name='test'),
    path('add_note/', views.add_note, name='add_note'),
]
