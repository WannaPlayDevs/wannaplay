# Generated by Django 2.0.4 on 2018-05-27 11:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Mensaje',
            fields=[
                ('pkMensaje', models.AutoField(primary_key=True, serialize=False)),
                ('asunto', models.TextField(max_length=150)),
                ('cuerpo', models.TextField(max_length=1000)),
                ('fecha', models.DateTimeField()),
                ('fkDestinatario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensaje_dest', to=settings.AUTH_USER_MODEL)),
                ('fkRemitente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='mensaje_rem', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
