from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.demo, name='demo'),
    path('new_interaction', views.new_interaction, name='new_interaction'),
    path('favorite', views.favorite, name='favorite'),
    path('popular', views.popular, name='popular'),
]
