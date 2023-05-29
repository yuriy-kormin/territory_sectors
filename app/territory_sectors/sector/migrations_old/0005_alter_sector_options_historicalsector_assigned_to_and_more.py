# Generated by Django 4.1.5 on 2023-02-27 11:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('status', '0001_initial'),
        ('sector', '0004_alter_historicalsector_name_alter_sector_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='sector',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='historicalsector',
            name='assigned_to',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='historicalsector',
            name='status',
            field=models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='status.status'),
        ),
        migrations.AddField(
            model_name='sector',
            name='assigned_to',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='sector',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='status.status'),
        ),
    ]