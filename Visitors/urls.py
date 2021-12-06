
from django.urls import path
from django.urls.conf import include
from .views import create_visitor , get_visitors_by_date , get_visitors_by_student_id
  
urlpatterns = [
        path("add_visitor",create_visitor),
        path("get_visitors_by_date/<str:search_date>",get_visitors_by_date),
        path("get_visitors_by_student_id/<str:student_id>",get_visitors_by_student_id),

]
