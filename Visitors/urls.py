
from django.urls import path
from django.urls.conf import include
from .views import create_visitor

urlpatterns = [
        path("create",create_visitor),

]