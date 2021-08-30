# Generated by Django 3.2.6 on 2021-08-30 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=90, verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Категория',
                'verbose_name_plural': 'Категории',
                'ordering': ['-title'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=200, verbose_name='Название')),
                ('description', models.TextField(default='', verbose_name='Описание')),
                ('date_start', models.DateTimeField(verbose_name='Дата начала')),
                ('participants_number', models.PositiveSmallIntegerField(default=0, verbose_name='Количество участников')),
                ('is_private', models.BooleanField(default=False, verbose_name='Частное')),
            ],
            options={
                'verbose_name': 'Событие',
                'verbose_name_plural': 'События',
                'ordering': ['-title'],
            },
        ),
    ]