# Generated by Django 4.1.7 on 2023-03-04 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0010_historicalhouse_for_search_historicalhouse_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='house/'),
        ),
    ]