# Generated by Django 5.0.2 on 2024-03-12 08:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_emailconfirmcodehelpermodel_deletion_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emailconfirmcodehelpermodel',
            name='deletion_time',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 12, 8, 48, 45, 690743, tzinfo=datetime.timezone.utc)),
        ),
    ]
