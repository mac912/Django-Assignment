from .views import CourseListView, CourseDetailListView
from django.urls import path, include

urlpatterns = [
    path('courses', CourseListView.as_view()),
    path('courses/<int:pk>', CourseDetailListView.as_view())
]