# Generated by Django 2.2.2 on 2019-12-10 09:26

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('car', '0003_cars_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='cars',
            name='year',
            field=models.IntegerField(),
        ),
    ]
