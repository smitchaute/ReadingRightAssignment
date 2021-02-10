from .views import RegisterAPI,LoginAPI,UserView
from django.urls import path, include
from knox import views as knox_views
from rest_framework import routers
from urllib import request

router=routers.DefaultRouter()
router.register('users',UserView)

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('',include(router.urls))
]