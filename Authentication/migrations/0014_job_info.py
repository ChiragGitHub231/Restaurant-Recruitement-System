# Generated by Django 4.1.7 on 2023-03-06 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0013_form_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Info',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('job_type', models.CharField(max_length=20)),
                ('first_name', models.CharField(default='', max_length=20)),
                ('last_name', models.CharField(default='', max_length=20)),
                ('contact_no', models.CharField(default='', max_length=10, unique=True)),
                ('email_id', models.EmailField(blank=True, default='', max_length=254, unique=True)),
                ('dob', models.CharField(default='', max_length=10)),
                ('address', models.TextField(default='')),
                ('zip_code', models.CharField(blank=True, default='', max_length=6)),
                ('city', models.CharField(default='', max_length=15)),
                ('state', models.CharField(default='', max_length=15)),
                ('aadhar_card', models.CharField(blank=True, default='', max_length=12, unique=True)),
                ('pan_card', models.CharField(blank=True, default='', max_length=10, unique=True)),
                ('availability', models.CharField(default='', max_length=10)),
                ('salary', models.CharField(default='', max_length=8)),
                ('experience', models.TextField(blank=True, default='')),
                ('add_info', models.TextField(null=True)),
                ('user_resume', models.FileField(default='', upload_to='')),
            ],
        ),
    ]
