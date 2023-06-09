# Generated by Django 4.2 on 2023-05-15 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(max_length=10000)),
                ('gpt', models.TextField(max_length=20000)),
            ],
        ),
        migrations.CreateModel(
            name='Operation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True)),
                ('pos_start', models.IntegerField(blank=True)),
                ('pos_end', models.IntegerField(blank=True)),
                ('comment', models.TextField(max_length=20000)),
            ],
        ),
    ]
