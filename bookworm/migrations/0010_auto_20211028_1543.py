# Generated by Django 3.2.8 on 2021-10-28 15:43

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookworm', '0009_remove_comment_obj_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='score',
            field=models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(0)]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.CharField(max_length=70, primary_key=1, serialize=False),
        ),
    ]
