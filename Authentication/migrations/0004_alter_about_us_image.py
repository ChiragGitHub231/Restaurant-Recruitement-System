# Generated by Django 4.1.7 on 2023-03-01 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0003_about_us'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_us',
            name='image',
            field=models.ImageField(upload_to='Authentication/static/images'),
        ),
    ]
