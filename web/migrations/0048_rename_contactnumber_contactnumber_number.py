# Generated by Django 3.2.18 on 2023-05-29 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0047_auto_20230529_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactnumber',
            old_name='contactNumber',
            new_name='number',
        ),
    ]