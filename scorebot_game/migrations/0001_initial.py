# Generated by Django 2.1.2 on 2018-10-26 03:05

from django.db import migrations, models
import django.db.models.deletion
import scorebot_core.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('scorebot_core', '0001_initial'),
        ('scorebot_grid', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Game Name')),
                ('start', models.DateTimeField(blank=True, null=True, verbose_name='Game Start Time')),
                ('finish', models.DateTimeField(blank=True, null=True, verbose_name='Game Finish Time')),
                ('scored', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Game Last Scored')),
                ('mode', models.SmallIntegerField(choices=[(0, 'Red-v-Blue'), (1, 'Blue-v-Blue'), (2, 'King'), (3, 'Rush'), (4, 'Defend')], default=0, verbose_name='Game Mode')),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'Stopped'), (1, 'Running'), (2, 'Paused'), (3, 'Canceled'), (4, 'Completed')], default=0, verbose_name='Game Status')),
                ('options', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scorebot_core.Options')),
            ],
            options={
                'verbose_name': 'Game',
                'verbose_name_plural': 'Games',
            },
        ),
        migrations.CreateModel(
            name='GameCompromise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('finish', models.DateTimeField(blank=True, null=True, verbose_name='Beacon Completed')),
                ('start', models.DateTimeField(auto_now_add=True, verbose_name='Beacon Start')),
                ('checkin', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Beacon Checkedin')),
            ],
            options={
                'verbose_name': 'Beacon',
                'verbose_name_plural': 'Beacons',
            },
        ),
        migrations.CreateModel(
            name='GameCompromiseHost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(null=True, unpack_ipv4=True, verbose_name='Host Address')),
                ('beacon', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='host', to='scorebot_game.GameCompromise')),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='beacons', to='scorebot_grid.Host')),
            ],
            options={
                'verbose_name': 'Beacon Host',
                'verbose_name_plural': 'Beacon Hosts',
            },
        ),
        migrations.CreateModel(
            name='GameEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeout', models.DateTimeField(verbose_name='Event Timeout')),
                ('data', models.TextField(blank=True, null=True, verbose_name='Event Data')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'Message'), (1, 'Window'), (2, 'Effect')], default=0, verbose_name='Event Type')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorebot_game.Game')),
            ],
            options={
                'verbose_name': '[Game] Event',
                'verbose_name_plural': '[Game] Events',
            },
        ),
        migrations.CreateModel(
            name='GameMonitor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('only', models.BooleanField(default=True, verbose_name='Monitor Only List')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorebot_game.Game')),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorebot_core.Monitor')),
                ('selected_hosts', models.ManyToManyField(blank=True, related_name='monitor', to='scorebot_grid.Host')),
            ],
            options={
                'verbose_name': '[Game] Monitor',
                'verbose_name_plural': '[Game] Monitors',
            },
        ),
        migrations.CreateModel(
            name='GamePort',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.PositiveSmallIntegerField(verbose_name='Port Number')),
            ],
            options={
                'verbose_name': '[Game] Beacon Port',
                'verbose_name_plural': '[Game] Beacon Ports',
            },
        ),
        migrations.CreateModel(
            name='GameScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flags', models.IntegerField(default=0, verbose_name='Flags')),
                ('uptime', models.IntegerField(default=0, verbose_name='Uptime')),
                ('tickets', models.IntegerField(default=0, verbose_name='Tickets')),
                ('beacons', models.IntegerField(default=0, verbose_name='Beacons')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Time')),
            ],
            options={
                'verbose_name': '[Game] Score',
                'verbose_name_plural': '[Game] Scores',
                'get_latest_by': 'date',
            },
        ),
        migrations.CreateModel(
            name='GameTeam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Team Name')),
                ('subnet', models.CharField(max_length=90, verbose_name='Team Subnet')),
                ('logo', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Team Logo')),
                ('offensive', models.BooleanField(default=False, verbose_name='Team is Offensive')),
                ('minimal', models.BooleanField(default=False, verbose_name='Team Score is Hidden')),
                ('color', models.IntegerField(default=scorebot_core.models.team_create_new_color, verbose_name='Team Color')),
                ('store', models.PositiveIntegerField(blank=True, null=True, unique=True, verbose_name='Team Store ID')),
                ('beacons', models.ManyToManyField(blank=True, editable=False, related_name='beacon_tokens', to='scorebot_core.Token')),
                ('dns', models.ManyToManyField(blank=True, to='scorebot_grid.DNS')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teams', to='scorebot_game.Game')),
                ('players', models.ManyToManyField(blank=True, related_name='game_teams', to='scorebot_core.Player')),
                ('score', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scorebot_core.Score')),
                ('token', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scorebot_core.Token')),
            ],
            options={
                'verbose_name': '[Game] Team',
                'verbose_name_plural': '[Game] Teams',
            },
        ),
        migrations.CreateModel(
            name='GameTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticket_id', models.PositiveIntegerField(verbose_name='Ticket ID')),
                ('name', models.CharField(max_length=150, verbose_name='Ticket Name')),
                ('closed', models.BooleanField(default=False, verbose_name='Ticket Closed')),
                ('started', models.DateTimeField(auto_now_add=True, verbose_name='Ticket Start')),
                ('total', models.PositiveIntegerField(default=0, verbose_name='Ticket Total Cost')),
                ('description', models.TextField(max_length=1000, verbose_name='Ticket Description')),
                ('type', models.PositiveSmallIntegerField(choices=[(0, 'No Category'), (1, 'Outage'), (2, 'Service Request'), (3, 'Change'), (4, 'Issue'), (5, 'Deliverable')], default=0, verbose_name='Ticket Category')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='scorebot_game.GameTeam')),
            ],
            options={
                'verbose_name': '[Game] Ticket',
                'verbose_name_plural': '[Game] Tickets',
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start', models.DateTimeField(auto_now_add=True, verbose_name='Job Start')),
                ('finish', models.DateTimeField(blank=True, null=True, verbose_name='Job Finish')),
                ('host', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='jobs', to='scorebot_grid.Host')),
                ('monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorebot_game.GameMonitor')),
            ],
            options={
                'verbose_name': 'Monitor Job',
                'verbose_name_plural': 'Monitor Jobs',
            },
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=150, verbose_name='Purchase Item')),
                ('amount', models.PositiveSmallIntegerField(verbose_name='Purchase Amount')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Purchase Date')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='purchases', to='scorebot_game.GameTeam')),
            ],
            options={
                'verbose_name': 'Purchase',
                'verbose_name_plural': 'Purchases',
            },
        ),
        migrations.AddField(
            model_name='gamescore',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scorebot_game.GameTeam'),
        ),
        migrations.AddField(
            model_name='gamecompromisehost',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='compromises', to='scorebot_game.GameTeam'),
        ),
        migrations.AddField(
            model_name='gamecompromise',
            name='attacker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attack_beacons', to='scorebot_game.GameTeam'),
        ),
        migrations.AddField(
            model_name='gamecompromise',
            name='token',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scorebot_core.Token'),
        ),
        migrations.AddField(
            model_name='game',
            name='ports',
            field=models.ManyToManyField(blank=True, editable=False, to='scorebot_game.GamePort'),
        ),
    ]
