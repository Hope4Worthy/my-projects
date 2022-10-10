from django.shortcuts import render, redirect
from django.views import generic
from .models import *


# Create your views here.

# ----- City Views ----- #
class City_detail_view(generic.DetailView):
    model 			= City_model
    template_name 	= 'city/City_detail.html'

class City_list_view(generic.ListView):
    model  			= City_model
    template_name 	= 'city/City_list.html'
    queryset = City_model.objects.all()


class City_add_view(generic.CreateView):
    model           = City_model
    template_name   = 'city/City_add.html'

    def form_valid(self, form):
        return redirect('City_list')

# ----- Location Views ----- #

class Location_detail_view(generic.DetailView):
    model  			= Location_model
    template_name 	= 'location/Location_detail.html'

class Location_list_view(generic.ListView):
    model  			= Location_model
    template_name 	= 'location/Location_list.html'

class Location_add_view(generic.CreateView):
    model           = Location_model
    template_name   = 'location/Location_add.html'

    def form_valid(self, form):
        return redirect('Location_list')

# ----- NPC Views ----- #

class Npc_detail_view(generic.DetailView):
    model  			= NPC_model
    template_name 	= 'npc/NPC_detail.html'

class Npc_list_view(generic.ListView):
    model  			= NPC_model
    template_name 	= 'npc/Npc_list.html'

class Npc_add_view(generic.CreateView):
    model           = NPC_model
    template_name   = 'npc/NPC_add.html'

    def form_valid(self, form):
        return redirect('NPC_list')

  # ----- Big Bad Views ----- #

# ----- Big Bad Views ----- #
 
class Big_Bad_detail_view(generic.DetailView):
    model  			= Big_Bad_model
    template_name 	= 'big_bad/Big_Bad_detail.html'

class Big_Bad_list_view(generic.ListView):
    model  			= Big_Bad_model
    template_name 	= 'big_bad/Big_Bad_list.html'

class Big_Bad_add_view(generic.CreateView):
    model           = Big_Bad_model
    template_name   = 'big_bad/Big_Bad_add.html'

    def form_valid(self, form):
        return redirect('Big_Bad_list')

# ----- Kingdom Views ----- #
   
class Kingdom_detail_view(generic.DetailView):
    model  			= Kingdom_model
    template_name 	= 'kingdom/Kingdom_detail.html'

class Kingdom_list_view(generic.ListView):
    model  			= Kingdom_model
    template_name 	= 'kingdom/Kingdom_list.html'

class Kingdom_add_view(generic.CreateView):
    model           = Kingdom_model
    template_name   = 'kingdom/Kingdom_add.html'

    def form_valid(self, form):
        return redirect('Kingdom_list')

# ----- Orginizations Views ----- #
        
class Orginization_detail_view(generic.DetailView):
    model  			= Orginization_model
    template_name 	= 'orginization/Orginization_detail.html'

class Orginization_list_view(generic.ListView):
    model  			= Orginization_model
    template_name 	= 'orginization/Orginization_list.html'

class Orginization_add_view(generic.CreateView):
    model           = Orginization_model
    template_name   = 'orginization/Orginization_add.html'

    def form_valid(self, form):
        return redirect('Orginization_list')

# ----- Quest Views ----- #
        
class Quest_detail_view(generic.DetailView):
    model  			= Quest_model
    template_name 	= 'quest/Quest_detail.html'

class Quest_list_view(generic.ListView):
    model  			= Quest_model
    template_name 	= 'quest/Quest_list.html'

class Quest_add_view(generic.CreateView):
    model           = Quest_model
    template_name   = 'quest/Quest_add.html'

    def form_valid(self, form):
        return redirect('Quest_list')

# ----- Dungeon Views ----- #
        
class Dungeon_detail_view(generic.DetailView):
    model  			= Dungeon_model
    template_name 	= 'dungeon/Dungeon_detail.html'

class Dungeon_list_view(generic.ListView):
    model  			= Dungeon_model
    template_name 	= 'dungeon/Dungeon_list.html'

class Dungeon_add_view(generic.CreateView):
    model           = Dungeon_model
    template_name   = 'dungeon/Dungeon_add.html'

    def form_valid(self, form):
        return redirect('Dungeon_list')

# ----- Large Threat Views ----- #

class Large_Threat_detail_view(generic.DetailView):
    model  			= Large_Threat_model
    template_name 	= 'large_threat/Large_Threat_detail.html'

class Large_Threat_list_view(generic.ListView):
    model  			= Large_Threat_model
    template_name 	= 'large_threat/Large_Threat_list.html'

class Large_Threat_add_view(generic.CreateView):
    model           = Large_Threat_model
    template_name   = 'large_threat/Large_Threat_add.html'

    def form_valid(self, form):
        return redirect('Large_Threat_list')

# ----- Fast Travel Route Views ----- #
        
class Fast_Travel_Route_detail_view(generic.DetailView):
    model  			= Fast_Travel_Route_model
    template_name 	= 'fast_travel_route/Fast_Travel_Route_detail.html'

class Fast_Travel_Route_list_view(generic.ListView):
    model  			= Fast_Travel_Route_model
    template_name 	= 'fast_travel_route/Fast_Travel_Route_list.html'

class Fast_Travel_Route_add_view(generic.CreateView):
    model           = Fast_Travel_Route_model
    template_name   = 'fast_travel_route/Fast_Travel_Route_add.html'

    def form_valid(self, form):
        return redirect('Fast_Travel_Route_list')

# ----- Shop Views ----- #     

class Shop_detail_view(generic.DetailView):
    model  			= Shop_model
    template_name 	= 'shop/Shop_detail.html'

class Shop_list_view(generic.ListView):
    model  			= Shop_model
    template_name 	= 'shop/Shop_list.html'

class Shop_add_view(generic.CreateView):
    model           = Shop_model
    template_name   = 'shop/Shop_add.html'

    def form_valid(self, form):
        return redirect('Shop_list')

# ----- Inn Views ----- #      

class Inn_detail_view(generic.DetailView):
    model  			= Inn_model
    template_name 	= 'inn/Inn_detail.html'

class Inn_list_view(generic.ListView):
    model  			= Inn_model
    template_name 	= 'inn/Inn_list.html'

class Inn_add_view(generic.CreateView):
    model           = Inn_model
    template_name   = 'inn/Inn_add.html'

    def form_valid(self, form):
        return redirect('Inn_list')

# ----- Tavern Views ----- #

class Tavern_detail_view(generic.DetailView):
    model  			= Tavern_model
    template_name 	= 'tavern/Tavern_detail.html'

class Tavern_list_view(generic.ListView):
    model  			= Tavern_model
    template_name 	= 'tavern/Tavern_list.html'

class Tavern_add_view(generic.CreateView):
    model           = Tavern_model
    template_name   = 'tavern/Tavern_add.html'

    def form_valid(self, form):
        return redirect('Tavern_list')
        