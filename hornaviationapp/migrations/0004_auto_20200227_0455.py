# Generated by Django 3.0.3 on 2020-02-27 04:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('hornaviationapp', '0003_auth_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='auth_user',
            name='date_joined',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='auth_user',
            name='superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='auth_user',
            name='username',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
    ]
