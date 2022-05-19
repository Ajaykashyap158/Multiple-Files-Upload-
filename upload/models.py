from os import system
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from upload.manager import UserManager

class User(AbstractUser):
    username=None
    email = models.EmailField(unique=True)
    is_verified=models.BooleanField(default=False)
    otp=models.CharField(max_length=4,null=True,blank=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, app_label):
        return self.is_superuser


class magazine_category(models.Model):
    category_id=models.IntegerField(primary_key=True)
    category_name=models.CharField(max_length=25)
    category_discription=models.CharField(max_length=25)
    def __str__(self):
        return self.category_name

class magazine_details(models.Model):
    magazine_id=models.IntegerField(primary_key=True)
    cover_image = models.ImageField(upload_to="Ajay", blank=True, null=True)
    file_name=models.CharField(max_length=25)
    discription=models.CharField(max_length=100)
    issue_date=models.DateField()
    rent_price=models.FloatField()
    buy_price=models.FloatField()
    rating=models.IntegerField()
    category_id=models.ForeignKey(magazine_category, related_name='meg_id', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.file_name
    
class magazine_Upload(models.Model):
    magazine_id = models.ForeignKey(magazine_details, related_name='meg_id', on_delete=models.CASCADE)
    File = models.FileField(upload_to=None)
    def meg_id(self):
        return self.magazine_id
