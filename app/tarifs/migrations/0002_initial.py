# Generated by Django 4.2.6 on 2023-10-18 16:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tarifs', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertarif',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_tarifs', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tarif',
            name='content',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tarifs', to='content.content'),
        ),
        migrations.AddField(
            model_name='tarif',
            name='user',
            field=models.ManyToManyField(through='tarifs.UserTarif', to=settings.AUTH_USER_MODEL),
        ),
    ]
