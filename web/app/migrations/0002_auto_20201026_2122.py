# Generated by Django 3.1.2 on 2020-10-26 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patients',
            name='active',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='alcohol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='cholesterol',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='gender',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='glucose',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='height',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='hight_pressure',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='low_pressure',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='smoker',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='patients',
            name='weight',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='cardio',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='patients',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
