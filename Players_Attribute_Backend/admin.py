from django.contrib import admin

# Register the models
from .models import Country, Club, Player

admin.site.register(Country)
admin.site.register(Club)
admin.site.register(Player)
