# Generated by Django 3.0.7 on 2020-09-27 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo_requirements', '0004_requirement_requirement_fulfilled'),
    ]

    operations = [
        migrations.AddField(
            model_name='requirement',
            name='fulfilled_by',
            field=models.ManyToManyField(related_name='fulfillers', to='ngo_requirements.Donor'),
        ),
    ]
