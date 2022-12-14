# Generated by Django 4.1.1 on 2022-09-20 11:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_rename_genreimageurl_genre_genresimageurl'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='arriveData',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Arrival Date'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='published',
            field=models.DateField(verbose_name='Published Date'),
        ),
    ]
