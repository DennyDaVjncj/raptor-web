# Generated by Django 4.1.5 on 2023-01-26 00:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authprofiles', '0005_remove_discorduserinfo_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='raptoruser',
            name='discord_user_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authprofiles.discorduserinfo'),
        ),
        migrations.AlterField(
            model_name='raptoruser',
            name='user_profile_info',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='authprofiles.userprofileinfo'),
        ),
    ]