from django.urls import path,include
from . import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register('students', views.StudentsViewSet, basename='students')
router.register('marks', views.MarksViewSet, basename='marks')


urlpatterns = [
    path('',include(router.urls) ),
]