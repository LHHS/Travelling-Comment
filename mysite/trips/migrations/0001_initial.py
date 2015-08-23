# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('comment', models.TextField()),
                ('photo', models.URLField()),
                ('location', models.CharField(max_length=100)),
                ('rating', models.DecimalField(decimal_places=1, max_digits=1)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('shirt_size', models.CharField(max_length=1, choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField(blank=True)),
                ('photo', models.URLField(blank=True)),
                ('required_time', models.IntegerField(default=0)),
                ('location', models.CharField(max_length=50)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='block',
            name='post',
            field=models.ForeignKey(to='trips.Post'),
            preserve_default=True,
        ),
    ]
