# Generated by Django 2.0.4 on 2018-05-27 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Amigo',
            fields=[
                ('pkAmigo', models.AutoField(primary_key=True, serialize=False)),
                ('fkUser1', models.IntegerField()),
                ('fkUser2', models.IntegerField()),
                ('estado', models.IntegerField()),
                ('fecha', models.DateTimeField()),
            ],
        ),
    ]
