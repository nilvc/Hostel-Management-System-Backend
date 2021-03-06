from django.urls import path,include
from knox import views as knox_views
from .views import RegisterApi,LoginApi,update_password

urlpatterns = [
    path("api/auth", include("knox.urls") ),
    path("api/auth/register", RegisterApi.as_view() ),
    path("api/auth/login", LoginApi.as_view() ),
    path("api/auth/logout", knox_views.LogoutView.as_view(),name="knox_logout" ),
    path("api/auth/update_password", update_password),
]