# Generated by Django 4.2.7 on 2023-11-25 22:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raptorbot', '0013_discordbotinternal_deleted_a_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discordbottasks',
            name='messages_to_delete',
            field=models.CharField(blank=True, default='', max_length=16300, null=True),
        ),
    ]