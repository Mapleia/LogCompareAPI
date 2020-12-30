# Generated by Django 3.1.4 on 2020-12-29 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('ID', models.IntegerField()),
                ('gw2Build', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Fight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.CharField(max_length=30)),
                ('DPS', models.IntegerField()),
                ('archetype', models.CharField(max_length=7)),
                ('b717', models.DecimalField(decimal_places=3, max_digits=6)),
                ('b718', models.DecimalField(decimal_places=3, max_digits=6)),
                ('b719', models.DecimalField(decimal_places=3, max_digits=6)),
                ('b725', models.DecimalField(decimal_places=3, max_digits=6)),
                ('b726', models.DecimalField(decimal_places=3, max_digits=6)),
                ('b740', models.DecimalField(decimal_places=3, max_digits=6)),
                ('b743', models.DecimalField(decimal_places=3, max_digits=6)),
                ('b873', models.DecimalField(decimal_places=3, max_digits=6)),
                ('b1122', models.DecimalField(decimal_places=3, max_digits=6)),
                ('b1187', models.DecimalField(decimal_places=3, max_digits=6)),
                ('b17674', models.DecimalField(decimal_places=3, max_digits=6)),
                ('b17675', models.DecimalField(decimal_places=3, max_digits=6)),
                ('b26980', models.DecimalField(decimal_places=3, max_digits=6)),
                ('b30328', models.DecimalField(decimal_places=3, max_digits=6)),
                ('fightID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maindb.encounter')),
            ],
        ),
    ]
