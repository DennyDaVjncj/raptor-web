# Generated by Django 4.2.3 on 2023-07-19 22:58

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('raptormc', '0034_alter_smallsiteinformation_ico_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='smallsiteinformation',
            name='ico_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='ICO', keep_meta=True, quality=5, scale=None, size=[64, 64], upload_to='ico'),
        ),
    ]
