from django.db.models import CharField, TextField, IntegerField, ForeignKey, ManyToManyField, CASCADE, Model

CITY_TYPES = (
	('CITY','city'),
	('TOWN','town'),
	('VILLAGE', 'village')
)

class City_model(Model):
	size 				 = CharField(choices=CITY_TYPES, default='CITY', max_length=8)
	name 				 = CharField(max_length=128)
	main_race 			 = CharField(max_length=128)
	main_exprt 			 = CharField(max_length=128)
	map_coordinate 		 = CharField(max_length=128)
	activites 			 = TextField()
	notes 				 = TextField()
	population 			 = IntegerField()

	def __str__(self):
		return self.name

class Location_model(Model):
	name 				 = CharField(max_length=128)
	map_coordinate 		 = CharField(max_length=128)
	category 			 = CharField(max_length=128)
	description 		 = TextField()
	notes 				 = TextField()

	def __str__(self):
		return self.name

class NPC_model(Model):
	resides_in 			 = ForeignKey(City_model, on_delete= CASCADE, related_name='npc_city', null=True)
	location 			 = ForeignKey(Location_model, on_delete= CASCADE, related_name='npc_location', null=True)
	name 				 = CharField(max_length=128)
	race 				 = CharField(max_length=128)
	gender				 = CharField(max_length=128)
	occupation 			 = CharField(max_length=128)
	apperance 			 = TextField()
	attitude 			 = TextField()
	age 				 = IntegerField()

	def __str__(self):
		return self.name
	
class Big_Bad_model(Model):
	resides_in 			 = ForeignKey(City_model, on_delete= CASCADE, related_name='bb_city', null=True)
	location 			 = ForeignKey(Location_model, on_delete= CASCADE, related_name='bb_location', null=True)
	name 				 = CharField(max_length=128)
	race 				 = CharField(max_length=128)
	gender				 = CharField(max_length=128)
	occupation 			 = CharField(max_length=128)
	apperance 			 = TextField()
	attitude 			 = TextField()
	goals 				 = TextField()
	age 				 = IntegerField()

	def __str__(self):
		return self.name

class Kingdom_model(Model):
	capitol 			 = ForeignKey(City_model, on_delete= CASCADE, related_name='kingdom_city')
	leader 				 = ForeignKey(NPC_model, on_delete= CASCADE, related_name='kingdom_npc')
	name 				 = CharField(max_length=128)
	government_type 	 = CharField(max_length=128)
	main_religion 		 = CharField(max_length=128)
	main_race 			 = CharField(max_length=128)
	relations 			 = TextField()
	notes 				 = TextField()

	def __str__(self):
		return self.name

class Orginization_model(Model):
	leader 				 = ForeignKey(NPC_model, on_delete= CASCADE, related_name='orginization_npc')
	operating_towns 	 = ManyToManyField(City_model)
	name 				 = CharField(max_length=128)
	relations 			 = TextField()
	notes 				 = TextField()

	def __str__(self):
		return self.name

class Quest_model(Model):
	giver 				 = ForeignKey(NPC_model, on_delete= CASCADE, related_name='quest_npc_giver')
	reciver 			 = ForeignKey(NPC_model, on_delete= CASCADE, related_name='quest_npc_reciver')
	town_of_origin 		 = ForeignKey(City_model, on_delete= CASCADE, related_name='quest_city')
	sponsor_org 		 = ForeignKey(Orginization_model, on_delete= CASCADE, related_name='quest_org', null=True)
	name 				 = CharField(max_length=128)
	category 			 = CharField(max_length=128)
	rewards 			 = TextField()
	description 		 = TextField()
	notes 				 = TextField()

	def __str__(self):
		return self.name

class Dungeon_model(Model):
	name 				 = CharField(max_length=128)
	map_coordinate 		 = CharField(max_length=128)
	dungen_boss 		 = CharField(max_length=128)
	other_creatures 	 = TextField()
	loot 				 = TextField()
	notes 				 = TextField()

	def __str__(self):
		return self.name

class Large_Threat_model(Model):
	name 				 = CharField(max_length=128)
	map_coordinate 		 = CharField(max_length=128)
	monster_type		 = CharField(max_length=128)
	loot 				 = TextField()

	def __str__(self):
		return self.name

class Fast_Travel_Route_model(Model):
	owner 				 = ForeignKey(Orginization_model, on_delete= CASCADE, related_name='fast_travel')
	connected_towns 	 = ManyToManyField(City_model)
	name 				 = CharField(max_length=128)
	cost 				 = CharField(max_length=128)
	risks 				 = TextField()
	notes 				 = TextField()

	def __str__(self):
		return self.name

class Shop_model(Model):
	location 			 = ForeignKey(City_model, on_delete= CASCADE, related_name='shop_city')
	owner 				 = ForeignKey(NPC_model, on_delete= CASCADE, related_name='shop_npc')
	name 				 = CharField(max_length=128)
	shop_type 			 = CharField(max_length=128)
	shop_class 			 = CharField(max_length=128)
	inventory 			 = TextField()

	def __str__(self):
		return self.name

class Inn_model(Model):
	location 			 = ForeignKey(City_model, on_delete= CASCADE, related_name='inn_location')
	owner 				 = ForeignKey(NPC_model, on_delete= CASCADE, related_name='inn_npc')
	name 				 = CharField(max_length=128)
	price_per_night 	 = CharField(max_length=128)
	name 				 = CharField(max_length=128)
	inventory 			 = TextField()

	def __str__(self):
		return self.name

class Tavern_model(Model):
	location 			 = ForeignKey(City_model, on_delete= CASCADE, related_name='tavern_city')
	owner 				 = ForeignKey(NPC_model, on_delete= CASCADE, related_name='tavern_npc')
	name 				 = CharField(max_length=128)
	inventory 			 = TextField()

	def __str__(self):
		return self.name
