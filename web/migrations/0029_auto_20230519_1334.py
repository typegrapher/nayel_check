# Generated by Django 3.2.18 on 2023-05-19 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0028_remove_home_aboutimg_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='feature1',
            field=models.CharField(max_length=200, null=True, verbose_name='Service feature 1'),
        ),
        migrations.AlterField(
            model_name='service',
            name='feature2',
            field=models.CharField(max_length=200, null=True, verbose_name='Service feature 2'),
        ),
        migrations.AlterField(
            model_name='service',
            name='feature3',
            field=models.CharField(max_length=200, null=True, verbose_name='Service feature 3'),
        ),
        migrations.AlterField(
            model_name='service',
            name='feature4',
            field=models.CharField(max_length=200, null=True, verbose_name='Service feature 4'),
        ),
        migrations.AlterField(
            model_name='service',
            name='feature5',
            field=models.CharField(max_length=200, null=True, verbose_name='Service feature 5'),
        ),
        migrations.AlterField(
            model_name='service',
            name='massage_1',
            field=models.CharField(max_length=150, null=True, verbose_name='Service more page content'),
        ),
    ]
