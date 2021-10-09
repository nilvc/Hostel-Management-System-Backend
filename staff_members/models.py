from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from students.models import Comlaint

# Create your models here.

class StaffProfile(models.Model):
    owner = models.OneToOneField(User , on_delete=models.CASCADE ,primary_key=True ,unique=True,editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mobilenum = models.BigIntegerField()

    def __str__(self):
        return self.owner.username


class Replie(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    owner = models.ForeignKey(StaffProfile ,on_delete= models.CASCADE , editable=False)
    date = models.DateField(auto_now_add=True)
    description = models.TextField()
    replying_to = models.ForeignKey(Comlaint , on_delete=models.CASCADE) 


    def short_serializer(self):
        return {
            "replied_by":{"name":self.owner.first_name , "id" : self.owner.owner.username},
            "description":self.description,
            "date":self.date
        }

    def __str__(self) -> str:
        return self.description

    







