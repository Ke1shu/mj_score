# Generated by Django 4.2.20 on 2025-04-30 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0005_remove_gamesettingmodel_rounding_rule_and_more'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='gamesettingmodel',
            constraint=models.UniqueConstraint(fields=('return_score', 'uma_2', 'uma_3', 'uma_4', 'tie_rule'), name='unique_game_setting'),
        ),
    ]
