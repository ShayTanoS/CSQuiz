# Generated by Django 5.0.2 on 2024-03-15 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quizapp', '0004_players_full_player_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='players',
            name='region',
            field=models.CharField(blank=True, default='Earth', max_length=90, null=True),
        ),
    ]
