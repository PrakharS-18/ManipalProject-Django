# Generated by Django 4.1 on 2022-10-22 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0007_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='Hospital_City',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Hospital_Email',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Hospital_Id',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Hospital_Location',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Hospital_Name',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Hospital_Number',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='Hospital_Password',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='UserType',
            field=models.CharField(default=None, max_length=500, null=True),
        ),
    ]