# Generated by Django 2.1.2 on 2018-10-26 03:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import scorebot_core.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.BigIntegerField(default=0, verbose_name='Key Access Level')),
            ],
            options={
                'verbose_name': 'Access Token',
                'verbose_name_plural': 'Access Tokens',
            },
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=75, verbose_name='Credit Name')),
                ('content', models.TextField(blank=True, max_length=2500, verbose_name='Credit HTML Code')),
            ],
            options={
                'verbose_name': 'Credit',
                'verbose_name_plural': 'Credits',
            },
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=150, verbose_name='Monitor Name')),
                ('access', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scorebot_core.AccessToken')),
            ],
            options={
                'verbose_name': 'Monitor',
                'verbose_name_plural': 'Monitors',
            },
        ),
        migrations.CreateModel(
            name='Options',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.SlugField(max_length=150, verbose_name='Preset Name')),
                ('ticket_cost', models.PositiveSmallIntegerField(default=50, verbose_name='Ticket Cost')),
                ('round_time', models.PositiveSmallIntegerField(default=300, verbose_name='Round Time (seconds)')),
                ('beacon_value', models.PositiveSmallIntegerField(default=100, verbose_name='Beacon Scoring Value')),
                ('ticket_max_score', models.PositiveSmallIntegerField(default=2400, verbose_name='Ticket Max Score')),
                ('flag_stolen_rate', models.PositiveSmallIntegerField(default=8400, verbose_name='Flag Stolen Rate')),
                ('host_ping_ratio', models.PositiveSmallIntegerField(default=50, verbose_name='Default Host Ping Percent')),
                ('beacon_time', models.PositiveSmallIntegerField(default=300, verbose_name='Default Beacon Timeout (seconds)')),
                ('job_timeout', models.PositiveSmallIntegerField(default=300, verbose_name='Unfinished Job Timeout (seconds)')),
                ('ticket_reopen_multiplier', models.PositiveSmallIntegerField(default=10, verbose_name='Ticket Reopen Multipler')),
                ('flag_captured_multiplier', models.PositiveSmallIntegerField(default=300, verbose_name='Flag Captured Multiplier')),
                ('job_cleanup_time', models.PositiveSmallIntegerField(default=900, verbose_name='Finished Job Cleanup Time (seconds)')),
                ('score_exchange_rate', models.PositiveIntegerField(default=100, verbose_name='Score to Coin Exchange Rate Percentage')),
                ('ticket_max_scoring', models.PositiveSmallIntegerField(default=14400, verbose_name='Ticket Max Scoring Time (seconds)')),
                ('ticket_grace_period', models.PositiveSmallIntegerField(default=900, verbose_name='Ticket Scoring Grace Period (seconds)')),
            ],
            options={
                'verbose_name': 'Game Preset',
                'verbose_name_plural': 'Game Presets',
            },
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Player Display Name')),
            ],
            options={
                'verbose_name': 'Player',
                'verbose_name_plural': 'Players',
            },
        ),
        migrations.CreateModel(
            name='Score',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flags', models.IntegerField(default=0, verbose_name='Flags')),
                ('uptime', models.IntegerField(default=0, verbose_name='Uptime')),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Time')),
                ('tickets', models.IntegerField(default=0, verbose_name='Tickets')),
                ('beacons', models.IntegerField(default=0, verbose_name='Beacons')),
            ],
            options={
                'verbose_name': 'Score',
                'verbose_name_plural': 'Scores',
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True, verbose_name='Team Name')),
                ('color', models.IntegerField(default=scorebot_core.models.team_create_new_color, verbose_name='Team Color')),
                ('last', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Team Last Game')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Team Registration')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='media', verbose_name='Team Logo')),
                ('players', models.ManyToManyField(blank=True, to='scorebot_core.Player')),
                ('score', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scorebot_core.Score')),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Teams',
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('expires', models.DateTimeField(blank=True, null=True, verbose_name='Token Expire')),
                ('uuid', models.UUIDField(default=scorebot_core.models.token_create_new_uuid, primary_key=True, serialize=False, verbose_name='Token ID')),
            ],
            options={
                'verbose_name': 'Token',
                'verbose_name_plural': 'Tokens',
                'get_latest_by': 'expires',
            },
        ),
        migrations.AddField(
            model_name='player',
            name='score',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scorebot_core.Score'),
        ),
        migrations.AddField(
            model_name='player',
            name='token',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scorebot_core.Token'),
        ),
        migrations.AddField(
            model_name='player',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='accesstoken',
            name='token',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scorebot_core.Token'),
        ),
    ]
