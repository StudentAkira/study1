# Generated by Django 4.1.3 on 2022-11-17 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_auth', '0004_alter_post_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=127),
        ),
    ]
