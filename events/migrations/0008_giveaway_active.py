# Generated by Django 3.0.6 on 2020-11-30 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_giveaway_whatsappgiveaway'),
    ]

    operations = [
        migrations.AddField(
            model_name='giveaway',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]