# Generated by Django 4.1.1 on 2022-09-08 15:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0012_alter_book_book_image_alter_book_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='desiredbook',
            name='ordered',
        ),
    ]