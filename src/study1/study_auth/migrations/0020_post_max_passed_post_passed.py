# Generated by Django 4.1.3 on 2022-11-30 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_auth', '0019_remove_post_int_field_remove_post_test_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='max_passed',
            field=models.IntegerField(default=10),
        ),
        migrations.AddField(
            model_name='post',
            name='passed',
            field=models.IntegerField(default=0),
        ),
    ]
