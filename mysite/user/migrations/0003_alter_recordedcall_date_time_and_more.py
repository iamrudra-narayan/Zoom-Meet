# Generated by Django 4.1.7 on 2023-03-01 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_recordedcall_recording_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recordedcall',
            name='date_time',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='recordedcall',
            name='duration',
            field=models.CharField(max_length=50),
        ),
    ]
