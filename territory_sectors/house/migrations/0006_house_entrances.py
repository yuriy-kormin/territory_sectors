# Generated by Django 4.1.5 on 2023-01-14 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_house_gps_point'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='entrances',
            field=models.IntegerField(null=True),
        ),
    ]
