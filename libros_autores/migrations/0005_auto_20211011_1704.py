# Generated by Django 3.2.7 on 2021-10-11 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros_autores', '0004_authors_notas'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='books_authors',
            name='id',
        ),
        migrations.AlterField(
            model_name='books_authors',
            name='author_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
