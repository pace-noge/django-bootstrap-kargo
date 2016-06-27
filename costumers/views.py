from django.contrib import messages
from django.core.urlresolvers import reverse
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404

from .models import Vehicle
from .forms import VehicleForm


def vehicle_list(request):
    """
    Showing list of vehicle in costumers page
    """

    # ORM for fetching all data
    vehicles = Vehicle.objects.all()

    # Dict returned by orm with key-value pair
    # column or field name as key
    context = {'vehicles': vehicles}

    return render(request, 'costumers/vehicle.html', context)


def create_vehicle(request):
    """
    Create new vehicle
    """

    # initial form context data

    context = {
        'form': VehicleForm(),
    }

    if request.method == "POST":

        # populate the form based POST DATA
        form = VehicleForm(request.POST, request.FILES)

        # transaction savepoint
        sid = transaction.savepoint()

        # vaidate the form
        if form.is_valid():

            vehicle_data = {
                'name': form.cleaned_data.get('name'),
                'driver': form.cleaned_data.get('driver'),
                'number': form.cleaned_data.get('number'),
                'capacity': form.cleaned_data.get('capacity'),
                'photo': form.cleaned_data.get('photo')
            }
            try:
                Vehicle.objects.create(**vehicle_data)
            except:
                transaction.savepoint_rollback(sid)
                messages.error(request, 'Ooop! Something Wrong Happened!')

            messages.info(request, "A new record has been created")

    return render(request, 'costumers/new_vehicle.html', context)


def edit_vehicle(request, pk=None):
    """
    redirect to list if pk is not valid
    """
    if not pk:
        return redirect(reverse('costumer:index'))

    # if record with the id is valid then return the object
    # else redirect to 404
    vehicle = get_object_or_404(Vehicle, pk=pk)

    # populate the form with existing data
    context = {
        'form': VehicleForm(instance=vehicle)
    }

    # if request method is post, update current record
    if request.method == 'POST':
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)

        # transaction save point
        sid = transaction.savepoint()

        if form.is_valid():
            try:
                form.save()
            except:
                transaction.savepoint_rollback(sid)
                messages.error(request, "Oops! Something wrong happened!")
            messages.info(request, "Record has been updated")
            return redirect(reverse('costumer:edit_vehicle', kwargs={'pk': pk}))
    return render(request, 'costumers/edit.html', context)


def delete_vehicle(request, pk=None):
    # get the record based on pk or return 404 instead
    if pk:
        vehicle = get_object_or_404(Vehicle, pk=pk)
        vehicle.delete()
        messages.success(request,  "Vehicle '{}'' has been deleted".format(vehicle.name))
    return redirect(reverse('costumer:index'))


