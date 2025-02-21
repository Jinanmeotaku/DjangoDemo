from django.shortcuts import render

# Create your views here.
# myapp/views.py
from django.http import HttpResponse

def new_route_view(request):
    return HttpResponse("Hello from the new route!")
