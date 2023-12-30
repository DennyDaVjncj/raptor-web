# Generated by Django 4.2.7 on 2023-12-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donations', '0008_completeddonation_completed'),
    ]

    operations = [
        migrations.AddField(
            model_name='completeddonation',
            name='checkout_id',
            field=models.CharField(default='', help_text='The unique ID for the Stripe Checkout session this Donation utilized.', max_length=1000, verbose_name='Stripe Checkout ID'),
        ),
    ]