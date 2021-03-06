# Generated by Django 3.0 on 2022-04-14 23:15

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
            name='University',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('domain', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('studentPopulation', models.IntegerField()),
                ('admin', models.ForeignKey(limit_choices_to={'groups': 3}, on_delete=django.db.models.deletion.CASCADE, related_name='uniAdmin', to=settings.AUTH_USER_MODEL)),
                ('students', models.ManyToManyField(blank=True, related_name='university', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-studentPopulation'],
            },
        ),
        migrations.CreateModel(
            name='Rso',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=250)),
                ('numberOfMembers', models.IntegerField(default=4)),
                ('status', models.CharField(choices=[('INACTIVE', 'inactive'), ('ACTIVE', 'active')], default='INACTIVE', max_length=8)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('owner', models.ForeignKey(blank=True, limit_choices_to={'groups': 2}, on_delete=django.db.models.deletion.CASCADE, related_name='rsoOwner', to=settings.AUTH_USER_MODEL)),
                ('students', models.ManyToManyField(blank=True, limit_choices_to={'groups': (1, 2)}, to=settings.AUTH_USER_MODEL)),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rsoUniversity', to='blog.University')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('description', models.TextField()),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locationUniversity', to='blog.University')),
            ],
            options={
                'ordering': ['-university'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved'), (2, 'Passed')], default=0)),
                ('day', models.DateField(help_text='Day of the event', verbose_name='Day of the event')),
                ('start_time', models.TimeField(help_text='Starting time', verbose_name='Starting time')),
                ('end_time', models.TimeField(help_text='Final time', verbose_name='Final time')),
                ('event_type', models.IntegerField(choices=[(1, 'public'), (2, 'rso'), (3, 'private')], default=1)),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('atendee', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='eventHost', to='blog.Rso')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Location')),
                ('university', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='university', to='blog.University')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('body', models.TextField()),
                ('rating', models.IntegerField(choices=[(1, 'poor'), (2, 'fair'), (3, 'average'), (4, 'good'), (5, 'great')], default=5)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Event')),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
