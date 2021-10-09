from django.urls import path
from .views import Create_staff_member,add_reply

urlpatterns = [
    path('add', Create_staff_member),
    path('reply', add_reply),
]