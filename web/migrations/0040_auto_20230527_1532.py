# Generated by Django 3.2.18 on 2023-05-27 10:02

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0039_auto_20230526_1436'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='career',
            name='detials_1_2',
        ),
        migrations.RemoveField(
            model_name='career',
            name='detials_1_3',
        ),
        migrations.RemoveField(
            model_name='career',
            name='detials_1_4',
        ),
        migrations.RemoveField(
            model_name='career',
            name='detials_1_5',
        ),
        migrations.RemoveField(
            model_name='career',
            name='detials_1_6',
        ),
        migrations.RemoveField(
            model_name='career',
            name='detials_1_7',
        ),
        migrations.RemoveField(
            model_name='career',
            name='detials_1_8',
        ),
        migrations.AlterField(
            model_name='career',
            name='detials_1_1',
            field=tinymce.models.HTMLField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='detials_2_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='detials_2_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='detials_2_3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='detials_2_4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='detials_2_5',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='detials_2_6',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='detials_2_7',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='detials_2_8',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='detials_3_1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='detials_3_2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='detials_3_3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='detials_3_4',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='detials_3_5',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='detials_3_6',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='detials_3_7',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='detials_3_8',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='career',
            name='points_headline_2',
            field=models.CharField(max_length=100, null=True, verbose_name='points headline 2'),
        ),
        migrations.AlterField(
            model_name='career',
            name='points_headline_3',
            field=models.CharField(max_length=100, null=True, verbose_name='points headline 3'),
        ),
    ]
