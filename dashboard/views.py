from django.shortcuts import render
from django.views import View
from .models import AdvertisementItem

class DashboardView(View):
    def get(self, request):
        items = AdvertisementItem.objects.all()
        return render(request, "dashboard/home.html", {"advertisement_items" : items, "cards" : items})
