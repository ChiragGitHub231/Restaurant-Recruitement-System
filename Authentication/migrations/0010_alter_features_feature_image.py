# Generated by Django 4.1.7 on 2023-03-01 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0009_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='feature_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
