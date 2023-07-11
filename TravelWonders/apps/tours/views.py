from django.shortcuts import render
from .models import Hotel, Tour, Hotel_detail

def hotel_list(request):
    hotel_list=Hotel.objects.all()
    return render(request, 'tours/list.html', {'hotel_list': hotel_list})

def tour_list(request):
    tour_list=Tour.objects.all()
    return render(request, 'tours/tour.html', {'tour_list': tour_list})

def hotel_detail(request):
    hotel_detail=Hotel_detail.objects.all()