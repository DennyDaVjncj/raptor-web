# Generated by Django 4.2.7 on 2023-11-18 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('raptormc', '0045_siteinformation_enable_server_query_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteinformation',
            name='discord_global_announcement_channel',
            field=models.IntegerField(default=0, help_text='Set this to the ID for the Discord Channel that the Bot will be looking for global announcements from.', verbose_name='The ID for the Global Announcements Discord Channel.'),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='discord_guild',
            field=models.IntegerField(default=6, help_text='Set this to the ID for the Discord Guild that the Bot will be reading global andserver announcements from.', verbose_name='The ID for the Discord Guild the Discord Bot will be associated with.'),
        ),
        migrations.AddField(
            model_name='siteinformation',
            name='discord_staff_role',
            field=models.IntegerField(default=0, help_text='Set this to the ID for the Discord Role that the Bot will read messages from as announcements. Discord Users without this role will not be able to create announcements. ', verbose_name='The ID for the Discord Role you designate as Staff.'),
        ),
    ]
