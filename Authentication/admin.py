from django.contrib import admin
from .models import User_Info, Contact_Us, About_Us, Services, Restaurant_Info, Gallary, Features, Form_Info, Job_Info

@admin.register(Contact_Us)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'description')

@admin.register(About_Us)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('message', 'image', 'item_detail')

@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('number', 'title', 'service_detail')

@admin.register(Restaurant_Info)
class Restaurant_InfoAdmin(admin.ModelAdmin):
    list_display = ('address', 'state', 'contact_1', 'contact_2', 'mail_1', 'mail_2')

@admin.register(Gallary)
class GallaryAdmin(admin.ModelAdmin):
    list_display = ('title', 'images')

@admin.register(Features)
class FeaturesAdmin(admin.ModelAdmin):
    list_display = ('feature_title', 'feature_image', 'feature_description')

@admin.register(Form_Info)
class Form_InfoAdmin(admin.ModelAdmin):
    list_display = ('form_title', 'first_name', 'last_name', 'contact_no', 'email_id', 'dob', 'address', 
    'zip_code', 'city', 'state', 'aadhar_card', 'pan_card', 'availability', 'salary', 'experience', 
    'add_info', 'resume', 'vacancy')

@admin.register(Job_Info)
class Job_InfoAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'job_type', 'first_name', 'last_name', 'contact_no', 'email_id', 'dob', 'address', 'zip_code', 
    'city', 'state', 'aadhar_card', 'pan_card', 'availability', 'salary', 'experience', 'add_info', 'user_resume')