# Generated by Django 5.1 on 2024-08-23 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pokemon', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='ability',
            field=models.CharField(default='Unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(max_length=100, unique=True),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(max_length=50),
        ),
    ]
