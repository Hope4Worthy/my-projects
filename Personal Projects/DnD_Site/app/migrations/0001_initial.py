# Generated by Django 3.1.6 on 2022-06-09 02:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('CITY', 'city'), ('TOWN', 'town'), ('VILLAGE', 'village')], default='CITY', max_length=8)),
                ('name', models.CharField(max_length=128)),
                ('main_race', models.CharField(max_length=128)),
                ('main_exprt', models.CharField(max_length=128)),
                ('map_coordinate', models.CharField(max_length=128)),
                ('activites', models.TextField()),
                ('notes', models.TextField()),
                ('population', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Dungeon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('map_coordinate', models.CharField(max_length=128)),
                ('dungen_boss', models.CharField(max_length=128)),
                ('other_creatures', models.TextField()),
                ('loot', models.TextField()),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Large_Threat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('map_coordinate', models.CharField(max_length=128)),
                ('monster_type', models.CharField(max_length=128)),
                ('loot', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('map_coordinate', models.CharField(max_length=128)),
                ('category', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('race', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=128)),
                ('occupation', models.CharField(max_length=128)),
                ('apperance', models.TextField()),
                ('attitude', models.TextField()),
                ('age', models.IntegerField()),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='npc_location', to='app.location')),
                ('resides_in', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='npc_city', to='app.city')),
            ],
        ),
        migrations.CreateModel(
            name='Orginization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relations', models.TextField()),
                ('notes', models.TextField()),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orginization_npc', to='app.npc')),
                ('operating_towns', models.ManyToManyField(to='app.City')),
            ],
        ),
        migrations.CreateModel(
            name='Tavern',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('inventory', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tavern_city', to='app.city')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tavern_npc', to='app.npc')),
            ],
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('shop_type', models.CharField(max_length=128)),
                ('shop_class', models.CharField(max_length=128)),
                ('inventory', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_city', to='app.city')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shop_npc', to='app.npc')),
            ],
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('category', models.CharField(max_length=128)),
                ('rewards', models.TextField()),
                ('description', models.TextField()),
                ('notes', models.TextField()),
                ('giver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quest_npc_giver', to='app.npc')),
                ('reciver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quest_npc_reciver', to='app.npc')),
                ('sponsor_org', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quest_org', to='app.orginization')),
                ('town_of_origin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quest_city', to='app.city')),
            ],
        ),
        migrations.CreateModel(
            name='kingdom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('government_type', models.CharField(max_length=128)),
                ('main_religion', models.CharField(max_length=128)),
                ('main_race', models.CharField(max_length=128)),
                ('level_corruption', models.CharField(max_length=128)),
                ('relations', models.TextField()),
                ('notes', models.TextField()),
                ('capitol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kingdom_city', to='app.city')),
                ('leader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kingdom_npc', to='app.npc')),
            ],
        ),
        migrations.CreateModel(
            name='Inn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_per_night', models.CharField(max_length=128)),
                ('name', models.CharField(max_length=128)),
                ('inventory', models.TextField()),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inn_location', to='app.city')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inn_mpc', to='app.npc')),
            ],
        ),
        migrations.CreateModel(
            name='Fast_Travel_Route',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.CharField(max_length=128)),
                ('risks', models.TextField()),
                ('notes', models.TextField()),
                ('connected_towns', models.ManyToManyField(to='app.City')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fast_travel', to='app.orginization')),
            ],
        ),
        migrations.CreateModel(
            name='Big_Bad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('race', models.CharField(max_length=128)),
                ('gender', models.CharField(max_length=128)),
                ('occupation', models.CharField(max_length=128)),
                ('apperance', models.TextField()),
                ('attitude', models.TextField()),
                ('goals', models.TextField()),
                ('age', models.IntegerField()),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bb_location', to='app.location')),
                ('resides_in', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bb_city', to='app.city')),
            ],
        ),
    ]
