from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.

class StaffProfile(models.Model):
    owner = models.OneToOneField(User , on_delete=models.CASCADE ,primary_key=True ,unique=True,editable=False)
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    mobilenum = models.BigIntegerField()

    def __str__(self):
        return self.owner.username



    def short_serializer(self):
        return {
            "name" : self.first_name +" "+ self.last_name
        }


    







