# Generated by Django 2.0 on 2017-12-10 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0003_auto_20171210_0505'),
    ]

    operations = [
        migrations.AddField(
            model_name='charm',
            name='order',
            field=models.PositiveSmallIntegerField(blank=True, default=0),
        ),
    ]
