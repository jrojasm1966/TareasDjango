# Generated by Django 3.2.7 on 2021-10-12 03:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Show',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Title*', max_length=255)),
                ('network', models.CharField(default='Network*', max_length=255)),
                ('release_date', models.DateField(default=datetime.datetime)),
                ('description', models.TextField(default='Descripcion')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]