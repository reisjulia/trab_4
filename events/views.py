from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
from .forms import EventForm

def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user  
            event.save()
            return redirect('index')  
    else:
        form = EventForm()
    return render(request, 'event_create.html', {'form': form})

def event_edit(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = EventForm(instance=event)
    return render(request, 'event_edit.html', {'form': form})

def event_delete(request, event_id):
    event = get_object_or_404(Event, pk=event_id)
    if request.method == 'POST':
        event.delete()
        return redirect('index')
    return render(request, 'event_delete.html', {'event': event})