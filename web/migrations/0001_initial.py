# Generated by Django 3.2.12 on 2023-06-01 05:53

from django.db import migrations, models
import tinymce.models
import versatileimagefield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=500)),
                ('subtitle', models.CharField(max_length=700)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='home-banner')),
            ],
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Blog image', verbose_name='Blog image')),
                ('detials_1', models.CharField(blank=True, max_length=70, null=True, verbose_name='Blog headline')),
                ('detials_2', models.CharField(blank=True, max_length=70, null=True, verbose_name='Blog content')),
                ('detials_3', models.CharField(blank=True, max_length=400, null=True, verbose_name='Blog content')),
                ('detials_4', models.CharField(blank=True, max_length=200, null=True, verbose_name='Blog content')),
            ],
            options={
                'verbose_name': 'Add Blog',
                'verbose_name_plural': 'Add Blogs',
            },
        ),
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='home-svc-baner')),
            ],
        ),
        migrations.CreateModel(
            name='Career',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='Career')),
                ('career', models.CharField(blank=True, max_length=100, null=True)),
                ('title', models.CharField(blank=True, max_length=100, null=True, verbose_name='Career title')),
                ('Introduction', models.CharField(max_length=500, null=True, verbose_name='Career Introduction')),
                ('points_headline_1', models.CharField(max_length=100, null=True, verbose_name='points headline 1')),
                ('detials_1_1', tinymce.models.HTMLField()),
                ('points_headline_2', models.CharField(max_length=100, null=True, verbose_name='points headline 2')),
                ('detials_2_1', tinymce.models.HTMLField()),
                ('points_headline_3', models.CharField(max_length=100, null=True, verbose_name='points headline 3')),
                ('detials_3_1', tinymce.models.HTMLField()),
            ],
        ),
        migrations.CreateModel(
            name='CareerApply',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Phone', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=254)),
                ('Message', models.TextField()),
                ('Qualification', models.CharField(max_length=100)),
                ('Career', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='home-banner')),
                ('career', models.CharField(max_length=500)),
                ('stories', models.TextField(max_length=700)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ContactNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(blank=True, null=True)),
                ('footernumber', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Home_aboutimg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(blank=True, null=True, upload_to='home-svc-baner')),
            ],
        ),
        migrations.CreateModel(
            name='MobileBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=300)),
                ('title', models.CharField(max_length=500)),
                ('subtitle', models.CharField(max_length=700)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='mobile-banner')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='HomeProject')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='service')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Service name')),
                ('massage', models.CharField(max_length=70, verbose_name='Service page content')),
                ('massage_1', models.CharField(max_length=150, null=True, verbose_name='Service more page content')),
                ('massage_2', models.CharField(max_length=70, null=True, verbose_name='Service more headline')),
                ('feature1', models.CharField(max_length=200, null=True, verbose_name='Service feature 1')),
                ('feature2', models.CharField(max_length=200, null=True, verbose_name='Service feature 2')),
                ('feature3', models.CharField(max_length=200, null=True, verbose_name='Service feature 3')),
                ('feature4', models.CharField(max_length=200, null=True, verbose_name='Service feature 4')),
                ('feature5', models.CharField(max_length=200, null=True, verbose_name='Service feature 5')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('service', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
