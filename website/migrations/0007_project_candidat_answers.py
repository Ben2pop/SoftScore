# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-16 10:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0007_auto_20171015_1502'),
        ('website', '0006_auto_20170918_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='candidat_answers',
            field=models.ManyToManyField(to='survey.Response'),
        ),
    ]