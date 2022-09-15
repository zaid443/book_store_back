# Generated by Django 4.1.1 on 2022-09-08 08:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='price')),
                ('best_seller', models.BooleanField(verbose_name='best_seller')),
                ('new_arrival', models.BooleanField(verbose_name='new_arrival')),
                ('top_rated', models.BooleanField(verbose_name='top_rated')),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='backend.author', verbose_name='category')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DesiredBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('qty', models.IntegerField(verbose_name='qty')),
                ('ordered', models.BooleanField(verbose_name='ordered')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.book', verbose_name='book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='DesiredBooks', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255, verbose_name='name')),
                ('image', models.ImageField(upload_to='category/', verbose_name='image')),
                ('is_active', models.BooleanField(verbose_name='is active')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('qty', models.DecimalField(blank=True, decimal_places=0, max_digits=1000, null=True, verbose_name='qty')),
                ('status', models.BooleanField(verbose_name='IsBought')),
                ('ordered', models.BooleanField(verbose_name='ordered')),
                ('DesiredBook', models.ManyToManyField(related_name='order', to='backend.desiredbook', verbose_name='DesiredBook')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='backend.genre', verbose_name='vendor'),
        ),
    ]
