# Generated by Django 2.2.5 on 2020-02-13 12:46

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Kategoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name_plural': 'kategorie',
            },
        ),
        migrations.CreateModel(
            name='Pytanie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tekst_pytania', models.CharField(max_length=200, verbose_name='tekst pytania')),
                ('data_d', models.DateTimeField(default=django.utils.timezone.now, verbose_name='data dodania pytania')),
                ('kategoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='pytania', to='ankiety.Kategoria')),
            ],
            options={
                'verbose_name_plural': 'pytania',
                'ordering': ['-data_d'],
            },
        ),
        migrations.CreateModel(
            name='Odpowiedz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tekst_odpowiedzi', models.CharField(max_length=200, verbose_name='tekst odpowiedzi')),
                ('glosy', models.IntegerField(default=0, verbose_name='liczba głosów')),
                ('pytanie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ankiety.Pytanie')),
            ],
            options={
                'verbose_name_plural': 'odpowiedzi',
            },
        ),
    ]
