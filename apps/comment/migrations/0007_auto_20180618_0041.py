# Generated by Django 2.0.2 on 2018-06-18 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0006_auto_20180618_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='object_id',
            field=models.PositiveIntegerField(verbose_name='博客ID'),
        ),
    ]
