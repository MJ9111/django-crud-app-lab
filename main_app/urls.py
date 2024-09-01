# urls.py

from django.urls import path
from . import views # Import views to connect routes to view functions

   


urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.cars_index, name='cars_index'),  
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),  
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/update/', views.car_update, name='car_update'),
    path('cars/<int:car_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
    path('cars/<int:car_id>/add_photo/', views.add_photo, name='add_photo'),
    path('cars/<int:car_id>/assoc_part/<int:part_id>/', views.assoc_part, name='assoc_part'),
    path('cars/<int:car_id>/unassoc_part/<int:part_id>/', views.unassoc_part, name='unassoc_part'),
    path('maintenance/', views.maintenance, name='maintenance'),
    path('parts/', views.PartList.as_view(), name='parts_index'),
    path('parts/<int:pk>/', views.PartDetail.as_view(), name='parts_detail'),
    path('parts/create/', views.PartCreate.as_view(), name='parts_create'),
    path('parts/<int:pk>/update/', views.PartUpdate.as_view(), name='parts_update'),
    path('parts/<int:pk>/delete/', views.PartDelete.as_view(), name='parts_delete'),
    path('maintenance/', views.maintenance_list, name='maintenance_list'),
    path('maintenance/', views.maintenance_list, name='maintenance'),
    path('maintenance/<int:maintenance_id>/', views.maintenance_detail, name='maintenance_detail'),
    path('maintenance/add/<int:car_id>/', views.add_maintenance, name='add_maintenance'), 
    path('maintenance/<int:maintenance_id>/edit/', views.maintenance_edit, name='maintenance_edit'), 
    path('maintenance/<int:maintenance_id>/delete/', views.maintenance_delete, name='maintenance_delete'),
    # path('cars/<int:car_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
    path('maintenance/', views.maintenance_list, name='maintenance_list'),  
    
]

    # path('cars/<int:car_id>/assoc_part/<int:part_id>/', views.assoc_part, name='assoc_part'),
    # path('cars/<int:car_id>/unassoc_part/<int:part_id>/', views.unassoc_part, name='unassoc_part'),
    # path('cars/<int:car_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
    # path('cars/', views.cars_index, name='cars_index'),
    # path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
    # path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    # path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    # path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),

    # path('parts/', views.PartList.as_view(), name='parts_index'),
    # path('parts/<int:pk>/', views.PartDetail.as_view(), name='parts_detail'),
    # path('parts/create/', views.PartCreate.as_view(), name='parts_create'),
    # path('parts/<int:pk>/update/', views.PartUpdate.as_view(), name='parts_update'),
    # path('parts/<int:pk>/delete/', views.PartDelete.as_view(), name='parts_delete'),


    # path('maintenance/', views.maintenance, name='maintenance'),
    # path('maintenance/', views.maintenance_list, name='maintenance_list'),
    # path('maintenance/<int:maintenance_id>/', views.maintenance_detail, name='maintenance_detail'),
    # path('maintenance/add/<int:car_id>/', views.add_maintenance, name='add_maintenance'), 
    # path('maintenance/<int:maintenance_id>/edit/', views.maintenance_edit, name='maintenance_edit'), 
    # path('maintenance/<int:maintenance_id>/delete/', views.maintenance_delete, name='maintenance_delete'),