# Generated by Django 5.0 on 2023-12-26 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0005_house_air_conditioning_house_backup_gen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='number_of_rooms',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='house',
            name='room_size',
            field=models.CharField(max_length=255),
        ),
    ]
