# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-09-23 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0100_auto_20180923_0523'),
    ]

    operations = [
        migrations.AddField(
            model_name='initialapplicationreview',
            name='incorrect_dates',
            field=models.BooleanField(default=False, verbose_name='Dates on time commitments look incorrect'),
        ),
        migrations.AddField(
            model_name='initialapplicationreview',
            name='missing_school',
            field=models.BooleanField(default=False, verbose_name='Essay mentioned school, but no school term info was supplied'),
        ),
        migrations.AddField(
            model_name='initialapplicationreview',
            name='missing_work',
            field=models.BooleanField(default=False, verbose_name='Essay mentioned work, but no work hours info was supplied'),
        ),
        migrations.AddField(
            model_name='initialapplicationreview',
            name='review_school',
            field=models.BooleanField(default=False, verbose_name='School term info needs review or follow up'),
        ),
        migrations.AddField(
            model_name='initialapplicationreview',
            name='review_work',
            field=models.BooleanField(default=False, verbose_name='Work time commitments need review or follow up'),
        ),
    ]