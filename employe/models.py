from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from phone_field import PhoneField
import qrcode
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.files import File
from django.utils import timezone
import random
import datetime
# Create your models here.

EMPLOYE_ROLE =(
        ('Software Enginnering','Software Enginnering'),
        ('Data Scientist','Data Scientist'),
        ('HR','HR'),
        ('Software Testing','Software Testing'),
        ('Backend Developer','Backend Developer'),
        ('Frontend Developer','Frontend Developer'),
        ('Cloud Enginnering','Cloud Enginnering')
    )
class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    email = models.EmailField()
    dob = models.DateField(blank=True,null=True)
    phone_number = PhoneField(blank=True, help_text='Contact phone number')
    employe_role = models.CharField(choices=EMPLOYE_ROLE,max_length=120)
    qrcode  = models.ImageField(blank=True)
    logout_time = models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return self.user.username

    def save(self,*args,**kwargs):
      qrcode_img=qrcode.make(self.user)
      canvas=Image.new("RGB", (300,300),"white")
      draw=ImageDraw.Draw(canvas)
      canvas.paste(qrcode_img)
      buffer=BytesIO()
      canvas.save(buffer,"PNG")
      self.qrcode.save(f'image{random.randint(0,9999)}',File(buffer),save=False)
      canvas.close()
      super().save(*args,**kwargs)

    def get_absoulte_url(self):
        return reverse("employe:detail",kwargs={'pk':self.pk})



class EmployeeWorkingHours(models.Model):
    user = models.ForeignKey(UserProfile,on_delete=models.CASCADE)
    start_time = models.DateTimeField(blank=True,null=True,default="0:00:00")
    end_time = models.DateTimeField(blank=True,null=True)

    

class FeedBack(models.Model):
    name = models.CharField(max_length=120)
    role = models.CharField(choices=EMPLOYE_ROLE,max_length=120)
    comments = models.TextField()


    def __str__(self):
        return self.name


class AdmintoUser(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    comments = models.TextField()
    sent_time = models.DateTimeField(blank=True,null=True,default=timezone.now())

