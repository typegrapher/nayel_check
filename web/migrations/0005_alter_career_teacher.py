# Generated by Django 4.2 on 2023-04-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_alter_career_detials'),
    ]

    operations = [
        migrations.AlterField(
            model_name='career',
            name='teacher',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
