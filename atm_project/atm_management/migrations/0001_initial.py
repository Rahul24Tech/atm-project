# Generated by Django 5.0.4 on 2024-04-22 06:13

import django.core.serializers.json
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cities', to='atm_management.state')),
            ],
        ),
        migrations.CreateModel(
            name='ATMSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('site_id', models.CharField(max_length=50, unique=True)),
                ('address', models.CharField(max_length=255)),
                ('contact_details', models.JSONField(encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atm_management.city')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='atm_management.state')),
            ],
        ),
    ]
