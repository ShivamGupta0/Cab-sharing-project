# Generated by Django 2.1 on 2020-04-11 16:44

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cabs', '0003_post_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='booked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='gender',
            field=models.CharField(choices=[('M', 'M'), ('F', 'F')], default='M', max_length=1),
        ),
        migrations.AlterField(
            model_name='post',
            name='passengers',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(3)]),
        ),
    ]