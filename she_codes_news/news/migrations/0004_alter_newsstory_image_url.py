# Generated by Django 3.2.5 on 2021-08-24 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20210824_1716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image_url',
            field=models.URLField(default='https://picum.photos/199', max_length=400),
        ),
    ]
