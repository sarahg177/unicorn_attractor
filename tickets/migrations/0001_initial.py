# Generated by Django 2.2.3 on 2019-07-08 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('issue_type', models.CharField(choices=[('Bug', 'Bug'), ('Feature', 'Feature')], default='Feature', max_length=7)),
                ('ticket_status', models.CharField(choices=[('Todo', 'Todo'), ('Doing', 'Doing'), ('Done', 'Done')], default='Todo', max_length=5)),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('completed_date', models.DateTimeField(blank=True, null=True)),
                ('description', models.TextField()),
                ('views', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_voted', models.DateTimeField(default=django.utils.timezone.now)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='ticket',
            name='upvotes',
            field=models.ManyToManyField(related_name='voter', through='tickets.Vote', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='ticket',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_commented', models.DateTimeField(default=django.utils.timezone.now)),
                ('comment', models.CharField(max_length=1000)),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tickets.Ticket')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]