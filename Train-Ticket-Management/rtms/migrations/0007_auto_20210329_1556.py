# Generated by Django 3.1.7 on 2021-03-29 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rtms', '0006_auto_20210329_1504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='reset_code',
            field=models.IntegerField(null=True),
        ),
    ]
