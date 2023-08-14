from django.urls import path
from . import views

app_name = 'Dj_app'

urlpatterns = [
    
    path('',views.home , name = "home"),
    path('today/',views.today, name= "today"),
    path('random/',views.random, name= "random"),
    path('random/password/',views.password, name= "password"),
    path('favs/',views.favs,name= "favs"),
    path('favs/games/',views.games,name= "games"),


]