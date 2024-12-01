from django.urls import path
from . import views

urlpatterns = [
    path('artists/', views.user_list, name='user_list'),
    path('artists/<int:pk>/', views.user_detail, name='user_detail'),
]
