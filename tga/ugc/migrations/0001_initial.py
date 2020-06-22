# Generated by Django 3.0.7 on 2020-06-05 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='KinoAfisha',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=70, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('producer', models.CharField(blank=True, max_length=70, null=True)),
                ('link', models.CharField(blank=True, max_length=130, null=True)),
            ],
            options={
                'db_table': 'kino_afisha',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Netflix',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=70, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('producer', models.CharField(blank=True, max_length=70, null=True)),
                ('link', models.CharField(blank=True, max_length=130, null=True)),
            ],
            options={
                'db_table': 'netflix',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Serials',
            fields=[
                ('id', models.AutoField(db_column='ID', primary_key=True, serialize=False)),
                ('title', models.CharField(blank=True, max_length=70, null=True)),
                ('description', models.CharField(blank=True, max_length=250, null=True)),
                ('producer', models.CharField(blank=True, max_length=70, null=True)),
                ('link', models.CharField(blank=True, max_length=130, null=True)),
            ],
            options={
                'db_table': 'serials',
                'managed': False,
            },
        ),
    ]
