# Generated by Django 5.0 on 2024-01-24 18:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_user_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='rendez_vous',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('avocat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.avocat')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.client')),
            ],
        ),
    ]