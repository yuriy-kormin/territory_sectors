# Generated by Django 4.1.7 on 2023-05-24 10:46

from django.db import migrations
import shortuuid.django_fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uuid',
            fields=[
                ('id', shortuuid.django_fields.ShortUUIDField(alphabet=None, auto_created=True, length=10, max_length=10, prefix='', primary_key=True, serialize=False)),
            ],
        ),
    ]
