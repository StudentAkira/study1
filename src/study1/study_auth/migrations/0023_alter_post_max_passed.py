# Generated by Django 4.1.3 on 2022-11-30 16:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_auth', '0022_alter_post_max_passed_alter_post_passed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='max_passed',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(1)]),
        ),
    ]