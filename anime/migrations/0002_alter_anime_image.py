# Generated by Django 3.2.9 on 2021-12-16 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anime', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='image',
            field=models.CharField(max_length=255),
        ),
    ]
