# Generated by Django 3.2.7 on 2021-10-10 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros_autores', '0003_remove_books_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notas',
            field=models.CharField(default='sin notas', max_length=255),
        ),
    ]
