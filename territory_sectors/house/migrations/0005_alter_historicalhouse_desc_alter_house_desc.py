# Generated by Django 4.1.5 on 2023-02-09 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0004_remove_historicalhouse_sector_remove_house_sector_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalhouse',
            name='desc',
            field=models.CharField(default='', max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='desc',
            field=models.CharField(default='', max_length=1500, null=True),
        ),
    ]
