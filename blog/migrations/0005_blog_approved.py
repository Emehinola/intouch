# Generated by Django 3.0.6 on 2020-12-05 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201128_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]