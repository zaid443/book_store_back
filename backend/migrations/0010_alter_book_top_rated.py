# Generated by Django 4.1.1 on 2022-09-08 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0009_remove_order_qty_book_saved_order_totalprice_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='top_rated',
            field=models.BooleanField(verbose_name='toprated'),
        ),
    ]
