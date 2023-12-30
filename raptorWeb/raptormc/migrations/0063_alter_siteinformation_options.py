# Generated by Django 4.2.7 on 2023-12-18 04:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('raptormc', '0062_siteinformation_navigation_from_top'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='siteinformation',
            options={'permissions': [('panel', 'Can access the Control Panel Homepage'), ('discord_bot', 'Can access the Discord Bot control panel'), ('server_actions', 'Can access the Server Actions menu'), ('reporting', 'Can access Reporting'), ('donations', 'Can access Donations'), ('settings', 'Can access settings (DANGEROUS!)')], 'verbose_name': ('Site Settings',), 'verbose_name_plural': 'Site Settings'},
        ),
    ]