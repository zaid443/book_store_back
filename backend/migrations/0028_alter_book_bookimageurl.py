# Generated by Django 4.1.1 on 2022-09-09 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0027_remove_book_savedbooks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookImageUrl',
            field=models.URLField(blank=True, default='https://upload.wikimedia.org/wikipedia/commons/thumb/9/98/Blank_button.svg/1200px-Blank_button.svg.png', null=True),
        ),
    ]