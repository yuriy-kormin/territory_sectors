# Generated by Django 4.1.5 on 2023-02-10 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0005_alter_historicalhouse_desc_alter_house_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalhouse',
            name='desc',
            field=models.CharField(blank=True, default='', max_length=1500, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='desc',
            field=models.CharField(blank=True, default='', max_length=1500, null=True),
        ),
    ]
