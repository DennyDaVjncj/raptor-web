# Generated by Django 4.2.7 on 2023-11-19 00:28

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('raptormc', '0051_alter_siteinformation_branding_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteinformation',
            name='background_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', help_text='The image displayed layered behind server buttons. This image will cover the defined Secondary Color if used. Optimal size for this image  is 1920x1080 or within the same aspect ratio.', keep_meta=False, quality=50, scale=None, size=[1920, 1080], upload_to='background', verbose_name='Background Image'),
        ),
    ]
