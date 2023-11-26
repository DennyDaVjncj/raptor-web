# Generated by Django 4.2.7 on 2023-11-25 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raptorbot', '0012_discordbottasks_messages_to_delete'),
    ]

    operations = [
        migrations.AddField(
            model_name='discordbotinternal',
            name='deleted_a_message',
            field=models.BooleanField(default=False, help_text='True if the Discord Bot deletes a message. Set back to Trueafter the delete receiver runs.'),
        ),
    ]
