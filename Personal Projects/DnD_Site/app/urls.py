
from .views import *
from django.urls import path
from .models import *

urlpatterns = [
	path('city/', 							City_list_view.as_view(), 					name='City_list'),
	path('city/add/', 						City_add_view.as_view(), 					name='City_add'),
	path('city/<int:pk>/', 					City_detail_view.as_view(), 				name='City_detail'),

	path('location/', 						Location_list_view.as_view(), 				name='Location_list'),
	path('location/add/', 					Location_add_view.as_view(), 				name='Location_add'),
	path('location/<int:pk>/', 				Location_detail_view.as_view(), 			name='Location_detail'),

	path('npc/', 							Npc_list_view.as_view(), 					name='Npc_list'),
	path('npc/add/', 						Npc_add_view.as_view(), 					name='Npc_add'),
	path('npc/<int:pk>/', 					Npc_detail_view.as_view(), 					name='Npc_detail'),

	path('big_bad/', 						Big_Bad_list_view.as_view(), 				name='Big_Bad_list'),
	path('big_bad/add/', 					Big_Bad_add_view.as_view(), 				name='Big_Bad_add'),
	path('big_bad/<int:pk>/', 				Big_Bad_detail_view.as_view(), 				name='Big_Bad_detail'),

	path('kingdom/', 						Kingdom_list_view.as_view(), 				name='Kingdom_list'),
	path('kingdom/add/', 					Kingdom_add_view.as_view(), 				name='Kingdom_add'),
	path('kingdom/<int:pk>/', 				Kingdom_detail_view.as_view(), 				name='Kingdom_detail'),

	path('orginization/', 					Orginization_list_view.as_view(), 			name='Orginization_list'),
	path('orginization/add/', 				Orginization_add_view.as_view(), 			name='Orginization_add'),
	path('orginization/<int:pk>/', 			Orginization_detail_view.as_view(), 		name='Orginization_detail'),

	path('quest/', 							Quest_list_view.as_view(), 					name='Quest_list'),
	path('quest/add/', 						Quest_add_view.as_view(), 					name='Quest_add'),
	path('quest/<int:pk>/', 				Quest_detail_view.as_view(), 				name='Quest_detail'),

	path('dungeon/', 						Dungeon_list_view.as_view(), 				name='Dungeon_list'),
	path('dungeon/add/', 					Dungeon_add_view.as_view(), 				name='Dungeon_add'),
	path('dungeon/<int:pk>/', 				Dungeon_detail_view.as_view(), 				name='Dungeon_detail'),

	path('large_threat/', 					Large_Threat_list_view.as_view(), 			name='Large_Threat_list'),
	path('large_threat/add/', 				Large_Threat_add_view.as_view(), 			name='Large_Threat_add'),
	path('large_threat/<int:pk>/', 			Large_Threat_detail_view.as_view(), 		name='Large_Threat_detail'),

	path('fast_travel_route/', 				Fast_Travel_Route_list_view.as_view(), 		name='Fast_Travel_Route_list'),
	path('fast_travel_route/add/', 			Fast_Travel_Route_add_view.as_view(), 		name='Fast_Travel_Route_add'),
	path('fast_travel_route/<int:pk>/', 	Fast_Travel_Route_detail_view.as_view(), 	name='Fast_Travel_Route_detail'),

	path('shop/', 							Shop_list_view.as_view(), 					name='Shop_list'),
	path('shop/add/', 						Shop_add_view.as_view(), 					name='Shop_add'),
	path('shop/<int:pk>/', 					Shop_detail_view.as_view(), 				name='Shop_detail'),

	path('inn/', 							Inn_list_view.as_view(), 					name='Inn_list'),
	path('inn/add/', 						Inn_add_view.as_view(), 					name='Inn_add'),
	path('inn/<int:pk>/', 					Inn_detail_view.as_view(), 					name='Inn_detail'),

	path('tavern/', 						Tavern_list_view.as_view(), 				name='Tavern_list'),
	path('tavern/add/', 					Tavern_add_view.as_view(), 					name='Tavern_add'),
	path('tavern/<int:pk>/', 				Tavern_detail_view.as_view(), 				name='Tavern_detail'),
]
