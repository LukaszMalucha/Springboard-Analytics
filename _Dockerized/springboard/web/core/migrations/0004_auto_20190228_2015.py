# Generated by Django 2.1.7 on 2019-02-28 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20190228_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='award',
        ),
        migrations.RemoveField(
            model_name='course',
            name='deadline',
        ),
        migrations.RemoveField(
            model_name='course',
            name='ects_credits',
        ),
        migrations.RemoveField(
            model_name='course',
            name='end_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='link',
        ),
        migrations.RemoveField(
            model_name='course',
            name='mode',
        ),
        migrations.RemoveField(
            model_name='course',
            name='nfq',
        ),
        migrations.RemoveField(
            model_name='course',
            name='ote_flag',
        ),
        migrations.RemoveField(
            model_name='course',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='course',
            name='skills',
        ),
        migrations.RemoveField(
            model_name='course',
            name='start_date',
        ),
    ]
