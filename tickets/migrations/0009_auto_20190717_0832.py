# Generated by Django 2.2.3 on 2019-07-17 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0008_auto_20190717_0830'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ticket',
            old_name='votes_total',
            new_name='votes',
        ),
    ]
