# Generated by Django 3.2.18 on 2023-05-18 11:58

from django.db import migrations
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0025_alter_home_aboutimg_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home_aboutimg',
            name='image',
            field=versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='home-svc-baner'),
        ),
    ]