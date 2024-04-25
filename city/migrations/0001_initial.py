# Generated by Django 4.2.9 on 2024-01-07 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city_name', models.CharField(blank=True, default=None, max_length=64, null=True)),
            ],
            options={
                'db_table': 'city',
            },
        ),
    ]
