from .views import GetAllCourseView,GetDetailCourseView
from django.urls import path

urlpatterns = [

    path('courses/',GetAllCourseView.as_view()),

    path('courses/<int:pk>/',GetDetailCourseView.as_view()),


]