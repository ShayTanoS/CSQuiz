# Generated by Django 5.0.2 on 2024-03-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_rename_userconfirmcodehelp_emailconfirmcodehelperform'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailConfirmCodeHelperModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('code', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('deletion_time', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='EmailConfirmCodeHelperForm',
        ),
    ]
