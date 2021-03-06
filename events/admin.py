from django.contrib import admin
from .models import EventModel, UserLikeEvent

@admin.register(EventModel, UserLikeEvent)
class AdminEventPage(admin.ModelAdmin):
    pass
