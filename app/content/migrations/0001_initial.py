# Generated by Django 4.2.6 on 2023-11-07 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BasePrice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Базовая стоимость')),
            ],
            options={
                'verbose_name': 'Базовая стоимость',
                'verbose_name_plural': 'Базовые стоимости',
            },
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Название контента')),
                ('coef', models.DecimalField(decimal_places=2, default=1, max_digits=5, verbose_name='Коэф контента')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='content.baseprice', verbose_name='цена контента')),
            ],
            options={
                'verbose_name': 'Тип Контента',
                'verbose_name_plural': 'Типы Контента',
            },
        ),
    ]
