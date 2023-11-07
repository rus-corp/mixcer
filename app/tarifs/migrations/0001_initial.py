# Generated by Django 4.2.6 on 2023-11-07 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название тарифа')),
                ('desc', models.TextField(max_length=900, verbose_name='Описание тарифа')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, verbose_name='базовая стоиость * на коэф контента')),
                ('shot_count', models.IntegerField(verbose_name='Количество кадров (шт)')),
                ('discount', models.DecimalField(decimal_places=2, default=0, max_digits=3)),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
            },
        ),
        migrations.CreateModel(
            name='UserTarif',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shot_remains', models.IntegerField(verbose_name='Остаток кадров')),
                ('tarif', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='user_tarifs', to='tarifs.tarif')),
            ],
            options={
                'verbose_name': 'Тариф пользователя',
                'verbose_name_plural': 'Тарифы Пользователей',
            },
        ),
    ]
