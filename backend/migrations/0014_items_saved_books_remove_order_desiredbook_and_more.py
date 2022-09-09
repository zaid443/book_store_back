# Generated by Django 4.1.1 on 2022-09-09 10:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('backend', '0013_remove_desiredbook_ordered'),
    ]

    operations = [
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('qty', models.IntegerField(default=1)),
                ('inCart', models.BooleanField(default=False)),
                ('isBought', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Saved_Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('saved', models.BooleanField(verbose_name='isSaved')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='order',
            name='DesiredBook',
        ),
        migrations.RemoveField(
            model_name='order',
            name='user',
        ),
        migrations.RemoveField(
            model_name='book',
            name='best_seller',
        ),
        migrations.RemoveField(
            model_name='book',
            name='new_arrival',
        ),
        migrations.RemoveField(
            model_name='book',
            name='saved',
        ),
        migrations.RemoveField(
            model_name='book',
            name='top_rated',
        ),
        migrations.AddField(
            model_name='book',
            name='total_sales',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DesiredBook',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.AddField(
            model_name='saved_books',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='books', to='backend.book', verbose_name='saved_Books'),
        ),
        migrations.AddField(
            model_name='saved_books',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='user_saved_Books'),
        ),
        migrations.AddField(
            model_name='items',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.book', verbose_name='book'),
        ),
        migrations.AddField(
            model_name='items',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DesiredBooks', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='book',
            name='savedBooks',
            field=models.ForeignKey(default=23, on_delete=django.db.models.deletion.DO_NOTHING, related_name='books', to='backend.saved_books', verbose_name='savedbook'),
            preserve_default=False,
        ),
    ]
