# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 20:43
from __future__ import unicode_literals

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('context', ckeditor.fields.RichTextField()),
            ],
            options={
                'verbose_name_plural': 'Cevaplar',
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Sorunuz')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Sorular',
            },
        ),
        migrations.CreateModel(
            name='SubAnswers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='realAnswer', to='app.Answers')),
                ('subanswer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subAnswer', to='app.Answers')),
            ],
            options={
                'verbose_name_plural': 'Alt Cevaplar',
            },
        ),
        migrations.CreateModel(
            name='UpDownVotesAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up_down', models.BooleanField()),
                ('answer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Answers')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UDAUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'UpDown Cevaplar',
            },
        ),
        migrations.CreateModel(
            name='UpDownVotesQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('up_down', models.BooleanField()),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Questions')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='UDQUser', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'UpDown Sorular',
            },
        ),
        migrations.AddField(
            model_name='answers',
            name='question_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionId', to='app.Questions'),
        ),
        migrations.AddField(
            model_name='answers',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userId', to=settings.AUTH_USER_MODEL),
        ),
    ]
