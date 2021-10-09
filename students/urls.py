from django.urls import path
from django.urls.conf import include
from .views import create_student , add_complaint , get_all_complaint,get_complaint,delete_complaint

urlpatterns = [
    path("create",create_student),
    path("add_complaint", add_complaint),
    path("get_all_complaints",get_all_complaint),
    path("get_complaint",get_complaint),
    path("delete_complaint",delete_complaint),
]
