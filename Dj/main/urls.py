from django.urls import path
from . import views

app_name = 'Dj_app'

urlpatterns = [
    
    path('',views.home),
    path('today/',views.today),
    path('random/',views.random),
    path('random/password/',views.password),
    path('favs/',views.favs),
    path('favs/games/',views.games),


]