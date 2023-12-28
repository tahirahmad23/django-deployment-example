# Generated by Django 5.0 on 2023-12-26 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accomodation', '0004_alter_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='air_conditioning',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='backup_gen',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='distance',
            field=models.CharField(default='0', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='electricity',
            field=models.CharField(default='0', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='runing_water',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='house',
            name='security_guards',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='N', max_length=255),
            preserve_default=False,
        ),
    ]