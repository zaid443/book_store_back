# Generated by Django 4.1.1 on 2022-09-09 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0023_alter_book_published_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateField(),
        ),
    ]
