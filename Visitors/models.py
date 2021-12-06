from django.db import models
import uuid
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from students.models import StudentProfile

# Create your models here.

class Visitor(models.Model):
    id = models.UUIDField(default=uuid.uuid4,primary_key=True,unique=True,editable=False)
    name = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True,editable=False)
    visiting_to = models.ForeignKey(StudentProfile ,on_delete=models.CASCADE, null=True , blank=True)
    mobile_num = models.BigIntegerField()
    in_time = models.TimeField(auto_now_add=True,editable=False)
    purpose_of_visiting = models.TextField(default="Not metioned")
    number_of_visitors = models.IntegerField(default=1)


    def __str__(self) -> str:
        return self.name + " "+ str(self.date)
    
    def serialize(self):
        name = self.visiting_to.name
        return {
            "id" : self.id,
            "name" : self.name,
            "date" : self.date,
            "visiting_to" : name,
            "mobile_number" : self.mobile_num,
            "in_time" : self.in_time,
            "purpose_of_visiting" : self.purpose_of_visiting,
            "number_of_visitors" : self.number_of_visitors
        }




    







