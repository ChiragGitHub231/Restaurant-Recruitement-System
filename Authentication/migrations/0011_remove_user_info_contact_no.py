# Generated by Django 4.1.7 on 2023-03-03 05:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0010_alter_features_feature_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_info',
            name='contact_no',
        ),
    ]
