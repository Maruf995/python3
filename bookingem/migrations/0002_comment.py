# Generated by Django 3.2.9 on 2021-12-01 17:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookingem', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=150)),
                ('blog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookingem.books')),
            ],
        ),
    ]
