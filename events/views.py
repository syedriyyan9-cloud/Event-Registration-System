from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import EventForm
from .models import Events

# Create your views here.
@login_required
def create_event(request):
    '''create event'''
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid:
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('users:profile')
        else:
            return HttpResponse('Failed to register event')
    else:
        form = EventForm()
    return render(request, 'events/create_event.html',{'form':form})

@login_required
def edit_event(request, pk):
    '''edit created event'''
    event = get_object_or_404(Events, pk = pk, user = request.user)
    if request.method == 'POST':
        form = EventForm(request.POST, instance=event)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = EventForm(instance=event)
    return render(request, 'events/edit_event.html', {'form':form, 'event':event})


