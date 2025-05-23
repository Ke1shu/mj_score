# Generated by Django 4.2.20 on 2025-04-30 23:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('score', '0004_roundmodel_override_tie_rule'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gamesettingmodel',
            name='rounding_rule',
        ),
        migrations.AddField(
            model_name='gamesettingmodel',
            name='name',
            field=models.CharField(default='hoge', max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gamesettingmodel',
            name='return_score',
            field=models.IntegerField(default=30000),
        ),
        migrations.AlterField(
            model_name='gamesettingmodel',
            name='tie_rule',
            field=models.CharField(choices=[('split', 'ウマを分配する'), ('prefer_early', '上位優先')], default='split', max_length=20),
        ),
        migrations.AlterField(
            model_name='gamesettingmodel',
            name='uma_2',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='gamesettingmodel',
            name='uma_3',
            field=models.IntegerField(default=-10),
        ),
        migrations.AlterField(
            model_name='gamesettingmodel',
            name='uma_4',
            field=models.IntegerField(default=-30),
        ),
    ]
