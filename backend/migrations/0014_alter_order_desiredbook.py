# Generated by Django 4.1.1 on 2022-09-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0013_remove_desiredbook_ordered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='DesiredBook',
            field=models.ManyToManyField(related_name='orders', to='backend.desiredbook', verbose_name='DesiredBook'),
        ),
    ]