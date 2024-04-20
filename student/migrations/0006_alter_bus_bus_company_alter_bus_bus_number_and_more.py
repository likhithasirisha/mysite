# Generated by Django 5.0.3 on 2024-04-05 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_bus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bus',
            name='bus_company',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='bus_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='bus_type',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='destination',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='bus',
            name='seats_available',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
