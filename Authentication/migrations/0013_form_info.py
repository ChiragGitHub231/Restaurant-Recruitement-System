# Generated by Django 4.1.7 on 2023-03-06 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0012_remove_user_info_id_alter_user_info_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('form_title', models.CharField(max_length=30)),
                ('first_name', models.BooleanField()),
                ('last_name', models.BooleanField()),
                ('contact_no', models.BooleanField()),
                ('email_id', models.BooleanField()),
                ('dob', models.BooleanField()),
                ('address', models.BooleanField()),
                ('zip_code', models.BooleanField()),
                ('city', models.BooleanField()),
                ('state', models.BooleanField()),
                ('aadhar_card', models.BooleanField()),
                ('pan_card', models.BooleanField()),
                ('availability', models.BooleanField()),
                ('salary', models.BooleanField()),
                ('experience', models.BooleanField()),
                ('add_info', models.BooleanField()),
                ('resume', models.BooleanField()),
                ('vacancy', models.BooleanField(default=False)),
            ],
        ),
    ]
