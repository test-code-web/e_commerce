# Generated by Django 3.1.12 on 2021-06-12 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0006_auto_20200724_0909'),
    ]

    operations = [
        migrations.AddField(
            model_name='partner',
            name='Company',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
