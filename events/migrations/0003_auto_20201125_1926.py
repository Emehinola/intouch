# Generated by Django 3.0.6 on 2020-11-25 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_vacancy'),
    ]

    operations = [
        migrations.AddField(
            model_name='vacancy',
            name='whatsapp_contact',
            field=models.CharField(default='none', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='requirements',
            field=models.TextField(),
        ),
    ]
