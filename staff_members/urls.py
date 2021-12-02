from django.urls import path
from .views import Create_staff_member,get_student,delete_student

urlpatterns = [
    path('add', Create_staff_member),
    path('get_student/<str:student_id>', get_student),
    path('delete_student/<str:student_id>', delete_student),
]