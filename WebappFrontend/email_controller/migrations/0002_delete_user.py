# Generated by Django 4.2.6 on 2023-11-04 16:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('email_controller', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]