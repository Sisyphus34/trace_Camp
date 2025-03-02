# Generated by Django 2.1.4 on 2019-01-04 20:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CardioTraining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('treadmill_time', models.TimeField()),
                ('treadmill_speed', models.FloatField()),
                ('treadmill_distance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='WeightTraining',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exercise', models.CharField(blank=True, choices=[('dl', 'Deadlift'), ('sq', 'Squat'), ('bp', 'Benchpress'), ('pd', 'Pulldown'), ('tm', 'Treadmill')], max_length=2)),
                ('reps', models.IntegerField()),
                ('weight', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('name', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='weighttraining',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puregainz.Workout'),
        ),
        migrations.AddField(
            model_name='cardiotraining',
            name='workout',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='puregainz.Workout'),
        ),
    ]
