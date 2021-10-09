from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from students.models import StudentProfile

# Create your models here.

class Visitor(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200,null=True)
    date = models.DateField(auto_now_add=True)
    visiting_to = models.ManyToManyField(StudentProfile)
    mobile_num = models.BigIntegerField()
    in_time = models.TimeField(auto_now_add=True,editable=False)
    out_time = models.TimeField(null=True)


    def __str__(self) -> str:
        return self.first_name




    







