# Generated by Django 3.2.18 on 2023-04-25 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20230424_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=500)),
                ('subtitle', models.CharField(max_length=700)),
            ],
        ),
    ]
