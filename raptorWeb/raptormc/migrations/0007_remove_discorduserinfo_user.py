# Generated by Django 3.2.5 on 2022-11-24 06:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raptormc', '0006_alter_userprofileinfo_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discorduserinfo',
            name='user',
        ),
    ]