from django.contrib import admin

from .models import Hotel, Tour, City, Hotel_detail, Advantage, Tourinfo

admin.site.register(Hotel)
admin.site.register(Tour)
admin.site.register(City)
admin.site.register(Hotel_detail)
admin.site.register(Advantage)
admin.site.register(Tourinfo)