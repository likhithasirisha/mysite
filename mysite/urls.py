"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from student.views import (student_list_view, 
                           update_student_view,
                           student_detail_view,
                           create_student_view,
                           delete_student_view,
                           employee_list_view,
                           create_employee_view,
                           employee_detail_view,
                           update_employee_view,
                           delete_employee_view,
                           movie_list_view,
                           create_movie_view,
                           movie_detail_view,
                           update_movie_view,
                           delete_movie_view,
                           car_list_view,
                           create_car_view,
                           car_detail_view,
                           update_car_view,
                           delete_car_view,
                           bus_list_view,
                           create_bus_view,
                           bus_detail_view,
                           update_bus_view,
                           delete_bus_view,
                           table_view,
                           card_view,
                           accordion_view,
                          )
                 
                                                                     


urlpatterns = [
    path('admin/', admin.site.urls),
    path('sl/', student_list_view),
    path('student-update/<int:id>/',update_student_view),
    path('student-detail/<int:id>/',student_detail_view),
    path('create-student/',create_student_view),
    path('delete-student/<int:id>/',delete_student_view),
    path('el/', employee_list_view),
    path('create-employee/',create_employee_view),
    path('employee-detail/<int:id>/',employee_detail_view),
    path('employee-update/<int:id>/',update_employee_view),
    path('delete-employee/<int:id>/',delete_employee_view),
    path('ml/', movie_list_view),
    path('create-movie/',create_movie_view),
    path('movie-detail/<int:id>/', movie_detail_view),
    path('movie-update/<int:id>/', update_movie_view),
    path('delete-movie/<int:id>/', delete_movie_view),
    path('cl/', car_list_view),
    path('create-car/',create_car_view),
    path('car-detail/<int:id>/', car_detail_view),
    path('car-update/<int:id>/', update_car_view),
    path('delete-car/<int:id>/', delete_car_view,),
    path('bl/', bus_list_view),
    path('', create_bus_view),
    path('bus-detail/<int:id>/',bus_detail_view),
    path('bus-update/<int:id>/', update_bus_view),
    path('delete-bus/<int:id>/', delete_bus_view),
    path('table/',table_view),
    path('card/',card_view),
    path('accordion/',accordion_view)

    
    
]
