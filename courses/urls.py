"""
URL configuration for courses project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from course.api.views import (
    CourseListView,
    CourseCreateAPIView,
    CourseRUDAPIView,
    EnrollCourseView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('drf-auth/', include('rest_framework.urls')),

    # Public view of courses
    path('courses/', CourseListView.as_view(), name='course-list'),

    # Create course
    path('courses/create/', CourseCreateAPIView.as_view(), name='course-create'),

    # Edit course
    path('courses/<int:pk>/', CourseRUDAPIView.as_view(), name='course-detail'),

    # Enroll on course
    path('courses/enroll/<int:course_id>/', EnrollCourseView.as_view(), name='course-enroll'),
]

