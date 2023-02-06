# Generated by Django 4.1.5 on 2023-02-06 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sector', '0003_historicalsector'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalsector',
            name='name',
            field=models.CharField(db_index=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='sector',
            name='name',
            field=models.CharField(max_length=300, null=True, unique=True),
        ),
    ]
