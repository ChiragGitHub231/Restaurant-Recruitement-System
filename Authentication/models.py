from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class User_Info(models.Model):
    username = models.CharField(primary_key=True, max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=15)

class Contact_Us(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    description = models.TextField()

class About_Us(models.Model):
    message = models.CharField(max_length=20)
    image = models.ImageField(upload_to="images/")
    item_detail = models.TextField()

class Services(models.Model):
    number = models.IntegerField()
    title = models.CharField(max_length=30)
    service_detail = models.TextField()

class Restaurant_Info(models.Model):
    address = models.TextField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    contact_1 = models.CharField(max_length=10, unique=True)
    contact_2 = models.CharField(max_length=10, unique=True)
    mail_1 = models.EmailField(unique=True)
    mail_2 = models.EmailField(unique=True)

class Gallary(models.Model):
    title = models.TextField()
    images = models.ImageField(upload_to="images/")

class Features(models.Model):
    feature_title = models.CharField(max_length=30)
    feature_description = models.TextField()
    feature_image = models.ImageField(upload_to="images/")

class Form_Info(models.Model):
    form_title = models.CharField(max_length=30)
    first_name = models.BooleanField()
    last_name = models.BooleanField()
    contact_no = models.BooleanField()
    email_id = models.BooleanField()
    dob = models.BooleanField()
    address = models.BooleanField()
    zip_code = models.BooleanField()
    city = models.BooleanField()
    state = models.BooleanField()
    aadhar_card = models.BooleanField()
    pan_card = models.BooleanField()
    availability = models.BooleanField()
    salary = models.BooleanField()
    experience = models.BooleanField()
    add_info = models.BooleanField()
    resume = models.BooleanField()
    vacancy = models.BooleanField(default=False)

class Job_Info(models.Model):
    user_id = models.AutoField(primary_key=True)
    job_type = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20, default="")
    last_name = models.CharField(max_length=20, default="")
    contact_no = models.CharField(max_length=10, unique=True, default="")
    email_id = models.EmailField(blank=True, unique=True, default="")
    dob = models.CharField(max_length=10, default="")
    address = models.TextField(default="")
    zip_code = models.CharField(max_length=6, blank=True, default="")
    city = models.CharField(max_length=15, default="")
    state = models.CharField(max_length=15, default="")
    aadhar_card = models.CharField(max_length=12, unique=True, blank=True, default="")
    pan_card = models.CharField(max_length=10, unique=True, blank=True, default="")
    availability = models.CharField(max_length=10, default="")
    salary = models.CharField(max_length=8, default="")
    experience = models.TextField(blank=True, default="")
    add_info = models.TextField(null=True)
    user_resume = models.FileField(default="")