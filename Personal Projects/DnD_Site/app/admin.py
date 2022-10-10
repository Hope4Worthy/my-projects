from django.contrib.admin import ModelAdmin, register
from .models import *

@register(City_model)
class City_admin(ModelAdmin):
	list_display = ('name',)

@register(Location_model)
class Location_admin(ModelAdmin):
	list_display = ('name',)

@register(NPC_model)
class NPC_admin(ModelAdmin):
	list_display = ('name',)

@register(Big_Bad_model)
class Big_Bad_admin(ModelAdmin):
	list_display = ('name',)

@register(Kingdom_model)
class Kingdom_admin(ModelAdmin):
	list_display = ('name',)

@register(Orginization_model)
class Orginization_admin(ModelAdmin):
	list_display = ('name',)

@register(Quest_model)
class Quest_admin(ModelAdmin):
	list_display = ('name',)

@register(Dungeon_model)
class Dungeon_admin(ModelAdmin):
	list_display = ('name',)

@register(Large_Threat_model)
class Large_Threat_admin(ModelAdmin):
	list_display = ('name',)

@register(Fast_Travel_Route_model)
class Fast_Travel_Route_admin(ModelAdmin):
	list_display = ('name',)

@register(Shop_model)
class Shop_admin(ModelAdmin):
	list_display = ('name',)

@register(Inn_model)
class Inn_admin(ModelAdmin):
	list_display = ('name',)

@register(Tavern_model)
class Tavern_admin(ModelAdmin):
	list_display = ('name',)
