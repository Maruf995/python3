# Generated by Django 3.2.9 on 2021-12-02 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookingem', '0002_comment'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Comments',
        ),
    ]
