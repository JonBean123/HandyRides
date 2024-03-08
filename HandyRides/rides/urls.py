from django.urls import path

from . import views

app_name = 'rides'
urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('create_rides', views.create_rides, name = 'create_rides'),
    path('search_results', views.display_rides, name = 'display_rides'),
    path('ai_interaction', views.ai_interaction, name = 'ai_interaction')
]

