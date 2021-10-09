from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
import staff_members.models as staff

# Create your models here.

class StudentProfile(models.Model):
    owner = models.OneToOneField(User , on_delete=models.CASCADE ,primary_key=True ,
                                unique=True , editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=20)
    mobilenum = models.BigIntegerField()
    roomnumber = models.IntegerField()
    created_by = models.ForeignKey("staff_members.StaffProfile",on_delete= models.CASCADE,default=None)


    def deepserialize(self):
        owner = self.owner
        return {
            "owner" : {"username":owner.username,"email":owner.email},
            "first_name":self.first_name,
            "branch":self.branch
        }

    def __str__(self):
        return self.owner.username



class Comlaint(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    owner = models.ForeignKey(StudentProfile ,on_delete = models.CASCADE , editable=False  )
    date = models.DateField(auto_now_add=True , editable=False)
    title = models.CharField(max_length=100,default=id)
    description = models.TextField()
    status = models.CharField(max_length=1,default="0")


    def short_serialize(self):
        return {
            "id":self.id,
            "title":self.title
        }


    def deep_serialize(self):
        owner = self.owner
        replies = staff.Replie.objects.filter(replying_to__id = self.id)
        replies = [replie.short_serializer() for replie in replies ]
        return {
            "owner":owner.owner.username,
            "first_name":owner.first_name,
            "branch":owner.branch,
            "title":self.title,
            "description": self.description,
            "date":self.date,
            "status":self.status,
            "replies":replies
        }

    def __str__(self) -> str:
        return self.description



    







