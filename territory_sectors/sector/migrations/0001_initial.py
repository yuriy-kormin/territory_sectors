# Generated by Django 4.1.5 on 2023-01-15 15:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('uuid_qr', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=300, null=True)),
                ('uuid', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='uuid_qr.uuid')),
            ],
        ),
    ]
