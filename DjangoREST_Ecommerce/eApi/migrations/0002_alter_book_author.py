# Generated by Django 4.0.1 on 2022-01-19 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.CharField(default='Dan Brown', max_length=100),
        ),
    ]
