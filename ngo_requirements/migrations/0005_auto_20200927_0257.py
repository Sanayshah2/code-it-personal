# Generated by Django 3.0.7 on 2020-09-26 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo_requirements', '0004_donations'),
    ]

    operations = [
        migrations.AddField(
            model_name='donations',
            name='kits',
            field=models.IntegerField(default=0, verbose_name='Number of kits'),
        ),
        migrations.AlterField(
            model_name='donations',
            name='beds',
            field=models.IntegerField(default=0, verbose_name='Number of beds'),
        ),
    ]
