from django.db import models
import uuid
from realone.settings import MEDIA_ROOT
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from staff_members.models import StaffProfile
# Create your models here.

class StudentProfile(models.Model):
    owner = models.OneToOneField(User , on_delete=models.CASCADE ,primary_key=True ,
                                unique=True , editable=False)
    name = models.CharField(max_length=200)
    branch = models.CharField(max_length=20)
    mobilenum = models.BigIntegerField()
    roomnumber = models.IntegerField()
    profile_pic = models.FileField(upload_to=MEDIA_ROOT , default= None)
    year        = models.IntegerField(default=1)
    created_by = models.ForeignKey(StaffProfile,on_delete= models.CASCADE,default=None)


    def deepserialize(self):
        owner = self.owner
        return {
            "registration_id" : owner.username,
            "email":owner.email,
            "name":self.name,
            "branch":self.branch,
            "profile_pic":str(self.profile_pic),
            "mobile_number" : self.mobilenum,
            "room_number" : self.roomnumber,
            "year" : self.year,
            "staff" : self.created_by.first_name + " " + self.created_by.last_name
        }

    def __str__(self):
        return self.owner.username



class Comlaint(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    owner = models.ForeignKey(StudentProfile ,on_delete = models.CASCADE , editable=False  )
    date = models.DateField(auto_now_add=True , editable=False)
    title = models.CharField(max_length=100,default=id)
    description = models.TextField()


    def short_serialize(self):
        return {
            "id":self.id,
            "title":self.title
        }


    def deep_serialize(self):
        owner = self.owner
        replie = Replie.objects.filter(replying_to__id = self.id)
        if len(replie)>0:
            replies =[rep.serializer() for rep in replie]
            replies = replies[0]
        else:
            replies = {"name" : "" , "description" : ""}
        return {
            "id" : self.id,
            "name":owner.name,
            "branch":owner.branch,
            "title":self.title,
            "description": self.description,
            "date":self.date,
            "replies":replies
        }

    def __str__(self) -> str:
        return self.title


class Replie(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    owner = models.ForeignKey(StaffProfile ,on_delete= models.CASCADE , editable=False)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    replying_to = models.ForeignKey(Comlaint , on_delete=models.CASCADE) 

    def serializer(self):
        name = self.owner.first_name +" "+ self.owner.last_name
        description = self.description
        return {
            "name" : name,
            "description" : description
        }
    







