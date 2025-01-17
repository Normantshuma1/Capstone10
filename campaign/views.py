from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Event

@login_required
def home(request):
    """
    Renders the home page for the campaign website.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: The rendered home page.
    """
    return render(request, 'campaign/home.html')

@login_required
def about(request):
    return render(request, 'campaign/about.html')

@login_required
def events(request):
    events = Event.objects.all()
    return render(request, 'campaign/events.html', {'events': events})
