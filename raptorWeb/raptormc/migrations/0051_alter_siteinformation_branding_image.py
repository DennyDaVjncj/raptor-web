# Generated by Django 4.2.7 on 2023-11-19 00:26

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('raptormc', '0050_alter_navwidget_nav_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinformation',
            name='branding_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', help_text='The image displayed in the website Navigation Bar as a link to the homepage. Optimal size for this image is w800xh200.', keep_meta=False, quality=50, scale=None, size=[550, 170], upload_to='branding', verbose_name='Branding Image'),
        ),
    ]
