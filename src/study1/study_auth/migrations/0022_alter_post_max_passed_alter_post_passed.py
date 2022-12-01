# Generated by Django 4.1.3 on 2022-11-30 16:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_auth', '0021_alter_post_passed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='max_passed',
            field=models.IntegerField(default=10, validators=[django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='post',
            name='passed',
            field=models.IntegerField(default=0),
        ),
    ]