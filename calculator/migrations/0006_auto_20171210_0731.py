# Generated by Django 2.0 on 2017-12-10 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calculator', '0005_auto_20171210_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='charm',
            name='description',
            field=models.TextField(default='t'),
        ),
        migrations.AlterField(
            model_name='charm',
            name='dice_description',
            field=models.TextField(default='t'),
        ),
    ]