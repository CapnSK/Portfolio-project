# Generated by Django 2.0.2 on 2020-05-26 12:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_job_uri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='uri',
            field=models.CharField(default="url 'home'", max_length=50),
        ),
    ]
