# Generated by Django 3.2 on 2023-05-19 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auction', '0004_auto_20230519_1510'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='acc_number',
        ),
    ]
