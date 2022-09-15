# Generated by Django 4.1.1 on 2022-09-09 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_alter_book_language'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='image',
            field=models.ImageField(default=1, upload_to='images/', verbose_name='image'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='is_active',
            field=models.BooleanField(default=1, verbose_name='is active'),
            preserve_default=False,
        ),
    ]
