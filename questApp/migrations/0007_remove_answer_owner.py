# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-11-12 22:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questApp', '0006_answer_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='owner',
        ),
    ]
