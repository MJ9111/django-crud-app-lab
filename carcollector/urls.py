# urls.py

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # Add this import
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from main_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('main_app.urls')),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cars/', views.CarList.as_view(), name='car_list'), 
    path('cars/', views.cars_index, name='cars_index'),
    path('cars/<int:car_id>/', views.car_detail, name='car_detail'),
    path('cars/create/', views.CarCreate.as_view(), name='cars_create'),
    path('cars/<int:pk>/update/', views.CarUpdate.as_view(), name='cars_update'),
    path('cars/<int:pk>/delete/', views.CarDelete.as_view(), name='cars_delete'),
    path('cars/<int:car_id>/add_maintenance/', views.add_maintenance, name='add_maintenance'),
    path('cars/<int:car_id>/add_photo/', views.add_photo, name='add_photo'),
    path('cars/<int:car_id>/assoc_part/<int:part_id>/', views.assoc_part, name='assoc_part'),
    path('cars/<int:car_id>/unassoc_part/<int:part_id>/', views.unassoc_part, name='unassoc_part'),
    path('parts/', views.PartList.as_view(), name='parts_index'),
    path('parts/<int:pk>/', views.PartDetail.as_view(), name='parts_detail'),
    path('parts/create/', views.PartCreate.as_view(), name='parts_create'),
    path('parts/<int:pk>/update/', views.PartUpdate.as_view(), name='parts_update'),
    path('parts/<int:pk>/delete/', views.PartDelete.as_view(), name='parts_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/login/', LoginView.as_view(), name='login'),  # Use Django's built-in LoginView
    path('accounts/logout/', LogoutView.as_view(), name='logout'),  # Use Django's built-in LogoutView
    path('accounts/profile/', views.profile, name='profile'),
    path('accounts/profile/edit/', views.profile_edit, name='profile_edit'),
    path('accounts/profile/delete/', views.profile_delete, name='profile_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', auth_views.LoginView.as_view(), name='login'),  # Add this line for the login view

]