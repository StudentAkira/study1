# Generated by Django 4.1.3 on 2022-11-30 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_auth', '0016_alter_post_test_text'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='int_field',
            field=models.IntegerField(default=0),
        ),
    ]