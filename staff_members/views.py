from students.models import Comlaint, Replie, StudentProfile
from django.shortcuts import render,get_list_or_404,get_object_or_404
from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse
from .models import  StaffProfile
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from knox.auth import TokenAuthentication
import json


# Create your views here.

def isauth(request):
    try:
        auth_header = request.headers['Authorization']
    except:
        return None

    token = auth_header[auth_header.index(' ')+1:]
    if not token:
        return None
    user = getUser(token)
    if not user:
        return None
    return user

def getUser(token):
    instance = TokenAuthentication()
    user = instance.authenticate_credentials(bytes(token,'utf-8'))[0]
    return user

def check_credentials(body):
    name = body["username"]
    email = body["email"]
    password = body["password"]
    if not name or not email or not password:
        return False
    return True
    

@api_view(['POST'])
def Create_staff_member(request):
    body = json.loads(request.body)
    if check_credentials(body):
        user = User.objects.create(
            username = body["username"],
            email = body["email"],
            password = make_password(body["password"]) 
        )
        user.save()
        staff_member = StaffProfile.objects.create(
            owner = user,
            first_name = body["first_name"],
            last_name = body["last_name"],
            mobilenum = body["mobile_number"],
        )
        staff_member.save()
        return HttpResponse("Staff member created")
    return HttpResponseBadRequest("Invalid Data")



@api_view(['GET'])
def get_student(request,student_id):
    try:
        if isauth(request):
            student = StudentProfile.objects.get(owner__username = student_id)
            return JsonResponse({"student" : student.deepserialize()})
        else:
            return HttpResponseBadRequest("Not authorized")
    except StudentProfile.DoesNotExist:
        return HttpResponseBadRequest("No such student")
    except:
        return HttpResponseBadRequest("Invalid data")



@api_view(['GET'])
def delete_student(request,student_id):
    try:
        print("ca")
        if isauth(request):
            student = User.objects.get(username = student_id)
            student.delete()
            return HttpResponse("Student deleted successfully")
        else:
            return HttpResponseBadRequest("Not authorized")
    except StudentProfile.DoesNotExist:
        return HttpResponseBadRequest("No such student")
    except:
        return HttpResponseBadRequest("Invalid data")










    


