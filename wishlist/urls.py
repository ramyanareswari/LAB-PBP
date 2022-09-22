from django.urls import path
from wishlist.views import show_wishlist, show_xml, show_json, show_json_id, show_xml_id, register, login_user, logout_user




app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', show_xml, name='show_xml'),
    path('xml/<int:id>', show_xml_id, name='show_xml_id'),
    path('json/', show_json, name='show_json'),
   
   path('logout/', logout_user, name='logout'), path('json/<int:id>', show_json_id, name='show_json_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]