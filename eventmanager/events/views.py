from os import name

from django.shortcuts import render, get_object_or_404, redirect
from .models import Event


def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html',
                  {'events': events})

def add_event(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        event_date = request.POST['event_date']
        location = request.POST['location']
        Event.objects.create(title=title, description=description,
                             event_date=event_date, location=location)
        return redirect('event_list')
    return render(request, 'add_event.html')

def edit_event(request, id):
    event = get_object_or_404(Event, id=id)
    if request.method == 'POST':
        event.title = request.POST['title']
        event.description = request.POST['description']
        event.event_date = request.POST['event_date']
        event.location = request.POST['location']
        event.save()
        return redirect('event_list')
    return render(request, 'edit_event.html',
                  {'event': event})

def delete_event(request, id):
    event = get_object_or_404(Event, id=id)
    event.delete()
    return redirect('event_list')
