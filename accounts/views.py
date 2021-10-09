from rest_framework import generics , permissions
from django.http.response import HttpResponse, HttpResponseBadRequest
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer,RegisterUserSerializer,LoginUserSerializer
from knox.auth import TokenAuthentication
from rest_framework.decorators import api_view
import json

from django.contrib.auth.models import User
from students.models import StudentProfile
from staff_members.models import StaffProfile

class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterUserSerializer
   

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "token":AuthToken.objects.create(user)[1],
            "user":UserSerializer(user,context=self.get_serializer_context()).data
        }) 


#login user
class LoginApi(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self,request,*args,**kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        is_student  = isStudent_or_Staff(user.username)
        return Response({
            "token":AuthToken.objects.create(user)[1],
            "user":UserSerializer(user,context=self.get_serializer_context()).data,
            "is_student":is_student
        }) 



def isStudent_or_Staff(username):
    try :
        print(username)
        student = StaffProfile.objects.get(username=username)
        return True
    except:
        return False




@api_view(["POST"])
def update_password(request):
    body = json.loads(request.body)
    password = body["password"] 
    user = User.objects.get(username = body["username"])
    print(password,body["password"],user)
    if user:
        user.set_password(password)
        user.save()
        return HttpResponse("Password updated")
    return HttpResponseBadRequest("Error")