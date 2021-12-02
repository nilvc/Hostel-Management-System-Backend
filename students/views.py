from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse
from .models import StudentProfile , Comlaint , Replie
from staff_members.models import StaffProfile
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.core.files.storage import FileSystemStorage
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


def check_credentials(request):
    try:
        name = request.POST.get("username")
        email = request.POST.get("email")
        if not name or not email :
            return False
        return True
    except:
        return False
    


@api_view(['POST'])
def create_student(request):
    try:
        staff = isauth(request)
        if not staff:
            return HttpResponseBadRequest("Not authorized")
        if check_credentials(request):
            user = User.objects.create(
                username = request.POST.get("username"),
                email = request.POST.get("email"),
                password = make_password(request.POST.get("username")) 
            )
            user.save()
            try:
                staff_member =StaffProfile.objects.get(owner__username = staff)
                file = request.FILES['profile_pic']
                fs = FileSystemStorage()
                filename = fs.save(file.name,file)
                file = fs.url(filename)
                student = StudentProfile.objects.create(
                    owner = user,
                    name = request.POST.get("name"),
                    branch = request.POST.get("branch"),
                    mobilenum = request.POST.get("mobile_number"),
                    roomnumber = request.POST.get("room_number"),
                    created_by = staff_member,
                    profile_pic = file,
                    year = request.POST.get("year")
                )
                student.save()
                return HttpResponse("Student registered successfully")
            except StaffProfile.DoesNotExist:
                return HttpResponseBadRequest("no")
            except:
                user.delete()
                return HttpResponseBadRequest("Invalid Data")
        else:
            return HttpResponseBadRequest("Invalid data")
    except:
        return HttpResponseBadRequest("Invalid Data")

@api_view(['POST'])
def add_complaint(request):
    try:
        body = json.loads(request.body)
        if isauth(request):
            owner = StudentProfile.objects.get(owner__username = isauth(request))
            complaint = Comlaint.objects.create(
                owner = owner,
                title = body["title"],
                description = body["description"]
            )
            complaint.save()
            return HttpResponse("complaint saved")
        else:
            return HttpResponseBadRequest("Not authorized")
    except StudentProfile.DoesNotExist:
        return HttpResponseBadRequest("No student with given data")
    except:
        return HttpResponseBadRequest("Invalid Data")


@api_view(['GET'])
def get_all_complaint(request):
    try:
        if isauth(request):
            complaints = Comlaint.objects.all()
            serializered = [complaint.deep_serialize() for complaint in complaints]
            return JsonResponse({"complaints":serializered})
        else:
            return HttpResponseBadRequest("Not authorized")
    except:
        return HttpResponseBadRequest("Some error occured")

@api_view(['GET'])
def get_my_complaints(request):
    try:
        user  = isauth(request)
        if user:
            complaints = Comlaint.objects.filter(owner__owner__username = user)
            serializered = [complaint.deep_serialize() for complaint in complaints]
            return JsonResponse({"complaints":serializered})
        else:
            return HttpResponseBadRequest("Not authorized")
    except:
        return HttpResponseBadRequest("Some error occured") 


@api_view(['GET'])
def get_complaint(request):
    try:
        body = json.loads(request.body)
        id = body["id"]
        complaint = Comlaint.objects.get(pk=id)
        return JsonResponse({'complaint':complaint.deep_serialize()},status=200,safe=False)
    except Comlaint.DoesNotExist:
        return HttpResponseBadRequest("Invalid complaint id")
    except :
        return HttpResponseBadRequest("Invalid Data")
    



@api_view(['GET'])
def delete_complaint(request):
    try:
        body = json.loads(request.body)
        id = body["id"]
        complaint = Comlaint.objects.get(pk=id)
        complaint.delete()
        return HttpResponse("Complaint deleted")
    except Comlaint.DoesNotExist:
        return HttpResponseBadRequest("Invalid complaint id")
    except :
        return HttpResponseBadRequest("Invalid Data")


@api_view(['POST'])
def add_reply(request):
    try:
        body = json.loads(request.body)
        staff = isauth(request)
        cowner = StaffProfile.objects.get(owner__username = staff)
        print(cowner)
        cdescription = body["description"]
        complaint_owner = Comlaint.objects.get(pk=body["id"])
        print(body["id"],complaint_owner)
        reply = Replie.objects.create(
            owner = cowner,
            description = cdescription,
            replying_to = complaint_owner
        )
        reply.save()
        return HttpResponse("Reply sent")
    except StaffProfile.DoesNotExist:
        return HttpResponseBadRequest("No such staff ")
    except Comlaint.DoesNotExist:
        return HttpResponseBadRequest("No such complaint")
    except:
        return HttpResponseBadRequest("Some error occured")
    
    


