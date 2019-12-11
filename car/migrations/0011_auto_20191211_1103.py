# Generated by Django 3.0 on 2019-12-11 10:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('seller', '0001_initial'),
        ('car', '0010_auto_20191210_1602'),
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=20)),
                ('brand', models.CharField(max_length=20)),
                ('year', models.IntegerField()),
                ('seller', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='cars', to='seller.Sellers')),
            ],
        ),
        migrations.DeleteModel(
            name='Cars',
        ),
    ]
