# Generated by Django 2.1.7 on 2019-03-17 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20190317_1244'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='updateddate',
            field=models.DateTimeField(blank=True),
        ),
    ]
