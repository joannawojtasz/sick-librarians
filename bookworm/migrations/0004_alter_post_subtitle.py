# Generated by Django 3.2.8 on 2021-10-24 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookworm', '0003_auto_20211024_2200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='subtitle',
            field=models.CharField(max_length=250),
        ),
    ]
