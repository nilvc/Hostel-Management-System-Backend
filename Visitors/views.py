from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse
from .models import Visitor
from students.models import StudentProfile
from rest_framework.decorators import api_view
import uuid
from knox.auth import TokenAuthentication
import json
from django.utils.dateparse import parse_date
import datetime



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
    try:
        body = json.loads(request.body)
        print("cam")
        student = StudentProfile.objects.get(owner__username = body["visiting_to"])
        visitor = Visitor(
                            name = body["name"],
                            mobile_num = body["mobile_number"],
                            purpose_of_visiting = body["purpose_of_visiting"],
                            number_of_visitors = body["number_of_visitors"],
                            visiting_to = student )
        visitor.save()
        return HttpResponse("Visitor saved successfully")
    except StudentProfile.DoesNotExist:
        return HttpResponseBadRequest("Invalid student id")

    except :
        return HttpResponseBadRequest("Error occured")
    
@api_view(['GET'])
def get_visitors_by_date(request,search_date):
    try:
        visitors = Visitor.objects.filter(date = search_date)
        all_visitor = []
        for visitor in visitors:
            all_visitor.append(visitor.serialize())
        return JsonResponse({"visitors" : all_visitor})
    except :
        return HttpResponseBadRequest("Error occured")

    
@api_view(['GET'])
def get_visitors_by_student_id(request,student_id):
    try:
        print(student_id)
        visitors = Visitor.objects.filter(visiting_to__owner__username = student_id)
        print(visitors)
        all_visitor = []
        for visitor in visitors:
            all_visitor.append(visitor.serialize())
        return JsonResponse({"visitors" : all_visitor})
    except :
        return HttpResponseBadRequest("Error occured")


