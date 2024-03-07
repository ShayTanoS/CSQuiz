# Generated by Django 5.0.2 on 2024-03-07 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Players',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_number', models.IntegerField(unique=True)),
                ('nickname', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=30)),
                ('surname', models.CharField(max_length=30)),
                ('age', models.IntegerField()),
                ('team', models.CharField(max_length=30)),
                ('major_winner', models.BooleanField()),
                ('major_mvp', models.BooleanField()),
            ],
        ),
    ]
