# Generated by Django 2.1.7 on 2019-03-30 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20190330_2215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Profile'),
        ),
    ]
