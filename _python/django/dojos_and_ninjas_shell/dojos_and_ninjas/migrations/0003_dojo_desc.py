# Generated by Django 2.2 on 2020-12-05 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojos_and_ninjas', '0002_auto_20201205_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='Old Dojo'),
        ),
    ]
