# Generated by Django 3.2.18 on 2023-05-12 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_auto_20230512_1519'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='feature5',
        ),
        migrations.RemoveField(
            model_name='service',
            name='feature6',
        ),
        migrations.RemoveField(
            model_name='service',
            name='feature7',
        ),
        migrations.RemoveField(
            model_name='service',
            name='feature8',
        ),
    ]