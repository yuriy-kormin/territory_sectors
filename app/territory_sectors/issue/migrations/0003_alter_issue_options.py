# Generated by Django 4.1.7 on 2023-04-01 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('issue', '0002_issue_completed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='issue',
            options={'ordering': ('date',)},
        ),
    ]
