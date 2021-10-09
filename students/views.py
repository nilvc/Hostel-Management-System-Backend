from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse
from .models import StudentProfile , Comlaint
from staff_members.models import StaffProfile
from rest_framework.decorators import api_view
from rest_framework.response import Response
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
def create_student(request):
    body = json.loads(request.body)
    if check_credentials(body):
        user = User.objects.create(
            username = body["username"],
            email = body["email"],
            password = make_password(body["password"]) 
        )
        user.save()
        
        staff_member =StaffProfile.objects.filter(owner__username = isauth(request))[0]
        student = StudentProfile.objects.create(
            owner = user,
            first_name = body["first_name"],
            last_name = body["last_name"],
            branch = body["branch"],
            mobilenum = body["mobile_number"],
            roomnumber = body["room_number"],
            created_by = staff_member,
        )
        student.save()
        return HttpResponse("Student registered successfully")
    return HttpResponseBadRequest("Invalid Data")

@api_view(['POST'])
def add_complaint(request):
    body = json.loads(request.body)
    cowner = StudentProfile.objects.get(owner__username = isauth(request))
    complaint = Comlaint.objects.create(
        owner = cowner,
        title = body["title"],
        description = body["description"]
    )
    complaint.save()
    return HttpResponse("complaint saved")


@api_view(['GET'])
def get_all_complaint(request):
    complaints = Comlaint.objects.all()
    serializered = [complaint.short_serialize() for complaint in complaints]
    return JsonResponse({"complaints":serializered})


@api_view(['GET'])
def get_complaint(request):
    body = json.loads(request.body)
    id = body["id"]
    complaint = Comlaint.objects.get(pk=id)
    return JsonResponse({'complaint':complaint.deep_serialize()},status=200,safe=False)
    



@api_view(['GET'])
def delete_complaint(request):
    body = json.loads(request.body)
    id = body["id"]
    complaint = Comlaint.objects.get(pk=id)
    complaint.delete()
    return HttpResponse("Complaint deleted")
    


