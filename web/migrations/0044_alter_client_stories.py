# Generated by Django 3.2.18 on 2023-05-29 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0043_auto_20230527_1548'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='stories',
            field=models.CharField(max_length=700),
        ),
    ]
