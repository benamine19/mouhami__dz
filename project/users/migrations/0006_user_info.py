# Generated by Django 5.0 on 2024-01-24 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_user_auth_provider'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='info',
            field=models.BooleanField(default=False),
        ),
    ]
