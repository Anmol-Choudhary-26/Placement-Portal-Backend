from django.contrib import admin
from .models import Slot

admin.site.register(Slot)

class SlotAdmin(admin.ModelAdmin):
  search_fields = ('booked_by__roll')