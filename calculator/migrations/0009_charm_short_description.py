# Generated by Django 2.0 on 2017-12-11 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0008_charm_ability'),
    ]

    operations = [
        migrations.AddField(
            model_name='charm',
            name='short_description',
            field=models.TextField(default='s'),
        ),
    ]
