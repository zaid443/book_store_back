# Generated by Django 4.1.1 on 2022-09-09 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0025_alter_book_published'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='bookImageUrl',
            field=models.URLField(blank=True, null=True),
        ),
    ]
