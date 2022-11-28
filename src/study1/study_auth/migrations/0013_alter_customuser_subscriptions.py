# Generated by Django 4.1.3 on 2022-11-28 14:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('study_auth', '0012_alter_customuser_subscriptions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='subscriptions',
            field=models.ManyToManyField(blank=True, null=True, related_name='subscriptions', to=settings.AUTH_USER_MODEL),
        ),
    ]
