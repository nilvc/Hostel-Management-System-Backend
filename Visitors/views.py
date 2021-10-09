from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse
from .models import Visitor
from students.models import StudentProfile
from rest_framework.decorators import api_view
import uuid
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
def create_visitor(request):
    body = json.loads(request.body)
    visitor = Visitor(
                        first_name = body["first_name"],
                        last_name = body["last_name"],
                        mobile_num = body["mobile_number"], )
    visitor.save()
    for username in body["visiting_to"]:
        student = StudentProfile.objects.get(owner__username = username)
        visitor.visiting_to.add(student)
    
    
    return HttpResponse("Visitor saved successfully")
    
@api_view(['POST'])
def set_out_time(request):
    try:
        body = json.loads(request.body)
        id = body["id"]
        visitor = Visitor.objects.get(pk=id)
        visitor.out_time = body["time"]
        visitor.save()
    except :
        return HttpResponseBadRequest("No visitor with this id")

    
    


