from django.urls import path
from . import views

urlpatterns = [
    path('hello/<str:name>', views.hello_world, name='hello_world'),
    path('hi/', views.hi_name, name='hi_name'),
    path('form', views.hello_form, name='hello_form'),
    path('student_list', views.student_list, name='student_list'),
    path('student_add', views.student_add, name='student_add'),
]
