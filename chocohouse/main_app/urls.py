from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('flavors/', views.flavors, name='flavors'),
    path('ingredients/', views.ingredients, name='ingredients'),
    path('feedback/', views.feedback, name='feedback'),
    path('delete-flvr/<int:flvr_id>/', views.delete_flvr, name='delete_flvr'),
    path('delete-ingr/<int:ingr_id>/', views.delete_ingr, name='delete_ingr'),
]
