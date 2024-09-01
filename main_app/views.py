# views.py
from django.urls import reverse_lazy  
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Car
from .models import Maintenance
from .models import Part
from .forms import CarForm
from .forms import MaintenanceForm
from .forms import PartForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User




def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def cars_index(request):
    cars = Car.objects.all()
    return render(request, 'cars/index.html', {'cars': cars})

def car_detail(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    return render(request, 'cars/detail.html', {'car': car})

def car_create(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save()
            return redirect('car_detail', car_id=car.id)
    else:
        form = CarForm()
    return render(request, 'cars/form.html', {'form': form})

def car_update(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('car_detail', car_id=car.id)
    else:
        form = CarForm(instance=car)
    return render(request, 'cars/form.html', {'form': form})

def car_delete(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        car.delete()
        return redirect('cars_index')
    return render(request, 'cars/delete.html', {'car': car})

def maintenance(request):
    maintenances = Maintenance.objects.all()
    cars = Car.objects.all()
    return render(request, 'main_app/maintenance.html', {'maintenances': maintenances, 'cars': cars})


class CarList(ListView):
    model = Car
    template_name = 'cars/car_list.html'
    # success_url = '/main/'
    context_object_name = 'cars'

class CarCreate(CreateView):
    model = Car
    fields = ['name', 'model', 'year']
    success_url = '/cars/'

class CarUpdate(UpdateView):
    model = Car
    fields = ['name', 'model', 'year']
    success_url = '/cars/'

class CarDelete(DeleteView):
    model = Car
    success_url = '/cars/'

class PartList(ListView):
    model = Part
    template_name = 'parts/index.html'
    context_object_name = 'parts'

class PartDetail(DetailView):
    model = Part
    template_name = 'parts/detail.html'
    context_object_name = 'part'

# @method_decorator(login_required, name='dispatch')
# class PartCreate(CreateView):
#     model = Part
#     fields = ['name', 'description', 'cars']
#     success_url = '/parts/'

@method_decorator(login_required, name='dispatch')
class PartCreate(CreateView):
    model = Part
    form_class = PartForm
    template_name = 'main_app/part_form.html'
    success_url = reverse_lazy('parts_index')

@method_decorator(login_required, name='dispatch')
class PartUpdate(UpdateView):
    model = Part
    form_class = PartForm
    template_name = 'main_app/part_form.html'
    success_url = reverse_lazy('parts_index')


@method_decorator(login_required, name='dispatch')
class PartDelete(DeleteView):
    model = Part
    template_name = 'main_app/part_confirm_delete.html'
    success_url = reverse_lazy('parts_index')

from django.shortcuts import render

def part_confirm_delete(request, part_id):
    part = get_object_or_404(Part, pk=part_id)
    if request.method == 'POST':
        part.delete()
        return redirect('parts_index')
    return render(request, 'main_app/part_confirm_delete.html')  
  
def add_maintenance(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        form = MaintenanceForm(request.POST)
        if form.is_valid():
            maintenance = form.save(commit=False)
            maintenance.car = car
            maintenance.save()
            return redirect('maintenance_detail', maintenance_id=maintenance.id)
    else:
        form = MaintenanceForm()
    return render(request, 'main_app/maintenance_form.html', {'form': form, 'car': car})

def maintenance_list(request):
    maintenances = Maintenance.objects.all()
    cars = Car.objects.all()
    return render(request, 'main_app/maintenance_list.html', {'maintenances': maintenances, 'cars': cars})

def maintenance(request):
    maintenances = Maintenance.objects.all()
    return render(request, 'main_app/maintenance.html', {'maintenances': maintenances})

def maintenance_detail(request, maintenance_id):
    maintenance = get_object_or_404(Maintenance, pk=maintenance_id)
    return render(request, 'main_app/maintenance_detail.html', {'maintenance': maintenance})

def maintenance_edit(request, maintenance_id):
    maintenance = get_object_or_404(Maintenance, pk=maintenance_id)
    if request.method == 'POST':
        form = MaintenanceForm(request.POST, instance=maintenance)
        if form.is_valid():
            form.save()
            return redirect('maintenance_detail', maintenance_id=maintenance.id)
    else:
        form = MaintenanceForm(instance=maintenance)
    return render(request, 'main_app/maintenance_form.html', {'form': form})

def maintenance_delete(request, maintenance_id):
    maintenance = get_object_or_404(Maintenance, pk=maintenance_id)
    if request.method == 'POST':
        maintenance.delete()
        return redirect('maintenance_list')
    return render(request, 'main_app/confirm_delete.html', {'maintenance': maintenance})

def add_photo(request, car_id):
    car = get_object_or_404(Car, pk=car_id)
    if request.method == 'POST':
        photo_url = request.POST.get('url')
        Photo.objects.create(url=photo_url, car=car)
        return redirect('car_detail', car_id=car.id)
    return render(request, 'cars/add_photo.html', {'car': car})

def assoc_part(request, car_id, part_id):
    car = get_object_or_404(Car, pk=car_id)
    part = get_object_or_404(Part, pk=part_id)
    car.parts.add(part)
    return redirect('car_detail', car_id=car.id)

def unassoc_part(request, car_id, part_id):
    car = get_object_or_404(Car, pk=car_id)
    part = get_object_or_404(Part, pk=part_id)
    car.parts.remove(part)
    return redirect('car_detail', car_id=car.id)


def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

@login_required
def profile(request):
    return render(request, 'registration/profile.html')

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserChangeForm(instance=request.user)
    return render(request, 'registration/profile_edit.html', {'form': form})

@login_required
def profile_delete(request):
    if request.method == 'POST':
        user = request.user
        user.delete()
        logout(request)
        return redirect('home')
    return render(request, 'registration/profile_delete.html')

