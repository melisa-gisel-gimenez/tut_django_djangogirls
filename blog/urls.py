from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list_1, name='post_list_1'),
]