# Generated by Django 3.0.6 on 2020-10-29 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addcv', '0007_person_tempid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='tempid',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
