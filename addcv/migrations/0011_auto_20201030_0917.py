# Generated by Django 3.0.6 on 2020-10-30 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addcv', '0010_auto_20201030_0854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temp',
            name='temp_id',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
    ]
