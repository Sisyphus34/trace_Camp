"""gainz URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from puregainz import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('gainz/create', views.WorkoutCreateView.as_view(), name = "workout_create"),
    path('gainz/list', views.WorkoutListView.as_view(), name = 'workout_list'),
    path('gainz/detail/<int:pk>', views.WorkoutDetailView.as_view(), name = "workout_detail"),
    path('gainz/delete/<int:pk>', views.WorkoutDeleteView.as_view(), name = "workout_delete"),
    path('gainz/update/<int:pk>', views.WorkoutUpdateView.as_view(), name = "workout_update"),
]
