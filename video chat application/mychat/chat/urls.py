from django.urls import path
from . import views


urlpatterns = [
    path('', views.lobby, name='lobby'),
    path('room/', views.room, name='room'),
    path('get-token/', views.getToken, name='getToken'),
    path('create-member/', views.createMember, name='createMember'),
    path('get-member/', views.getMember, name='getMember'),
    path('delete-member/', views.deleteMember, name='deleteMember'),
]
