# Generated by Django 3.0.8 on 2020-07-28 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_opis'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='opis',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]