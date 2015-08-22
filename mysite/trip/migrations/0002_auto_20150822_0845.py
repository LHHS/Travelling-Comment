# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.TextField()),
                ('photo', models.URLField()),
                ('location', models.CharField(max_length=100)),
                ('rating', models.DecimalField(max_digits=1, decimal_places=1)),
            ],
        ),
        migrations.RenameField(
            model_name='post',
            old_name='created_at',
            new_name='created_date',
        ),
        migrations.AddField(
            model_name='post',
            name='required_time',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='block',
            name='post',
            field=models.ForeignKey(to='trip.Post'),
        ),
    ]
