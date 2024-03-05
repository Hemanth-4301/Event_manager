from django.shortcuts import render,redirect
from django.http import HttpResponse

def hello(request):
    return render(request,'home.html')
# Create your views here.

def image(request):
    # Add any necessary logic here
    return render(request, 'image.html')

from .models import Event

def add_event(request):
    if request.method == 'POST':
        date = request.POST.get('date')
        month = request.POST.get('month')
        name = request.POST.get('name').lower()
        
        # Check if the event already exists
        if not Event.objects.filter(date=date, month=month, name=name).exists():
            # Event does not exist, so save it
            event = Event(date=date, month=month, name=name)
            event.save()
            content = "Event added successfully!"
            html_content = f"<div style='font-size: 50px;'>{content}</div>"
            return HttpResponse(html_content)
        else:
            content = "Event already exists!"
            html_content = f"<div style='font-size: 50px;'>{content}</div>"
            return HttpResponse(html_content)
    return render(request, 'add_event.html')


def display_events(request):
    if request.method == 'POST':
        month = request.POST.get('month')
        events = Event.objects.filter(month=month)
        if not events:
            message = f"No events found for month {month}."
        else:
            message = None
        return render(request, 'display_events.html', {'events': events, 'message': message})
    return render(request, 'select_month.html')
