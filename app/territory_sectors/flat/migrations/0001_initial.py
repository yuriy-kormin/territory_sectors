# Generated by Django 4.1.7 on 2023-05-24 10:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('language', '0001_initial'),
        ('uuid_qr', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalFlat',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('date_joined', models.DateTimeField(blank=True, editable=False)),
                ('date_modified', models.DateTimeField(blank=True, editable=False)),
                ('number', models.CharField(blank=True, max_length=300, null=True)),
                ('entrance', models.IntegerField(blank=True, null=True)),
                ('floor', models.IntegerField(blank=True, null=True)),
                ('way_desc', models.CharField(max_length=1500)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('house', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='house.house')),
                ('language', models.ForeignKey(blank=True, db_constraint=False, default=1, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='language.language')),
                ('uuid', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='uuid_qr.uuid')),
            ],
            options={
                'verbose_name': 'historical flat',
                'verbose_name_plural': 'historical flats',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Flat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('number', models.CharField(blank=True, max_length=300, null=True)),
                ('entrance', models.IntegerField(blank=True, null=True)),
                ('floor', models.IntegerField(blank=True, null=True)),
                ('way_desc', models.CharField(max_length=1500)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='house.house')),
                ('language', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='language.language')),
                ('uuid', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='uuid_qr.uuid')),
            ],
            options={
                'ordering': ['house', 'entrance', 'floor', 'number'],
            },
        ),
    ]
