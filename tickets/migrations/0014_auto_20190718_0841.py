# Generated by Django 2.2.3 on 2019-07-18 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0013_ticket_money_raised'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='money_raised',
            field=models.IntegerField(default=0),
        ),
    ]
