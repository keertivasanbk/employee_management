# Generated by Django 4.1.2 on 2022-11-20 11:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("employe", "0012_alter_admintouser_sent_time"),
    ]

    operations = [
        migrations.AddField(
            model_name="feedback",
            name="sent_time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2022, 11, 20, 11, 26, 8, 187537),
                null=True,
            ),
        ),
        migrations.AlterField(
            model_name="admintouser",
            name="sent_time",
            field=models.DateTimeField(
                blank=True,
                default=datetime.datetime(2022, 11, 20, 11, 26, 8, 187770),
                null=True,
            ),
        ),
    ]