from django.contrib import admin
from .models import Beeyards, Hives, Intervention

class BeeyardAdmin(admin.ModelAdmin):
  list_display=('name','user')
  list_filter=('name', 'user')
  search_fields=('name', 'user')

admin.site.register(Beeyards, BeeyardAdmin)

class HivesAdmin(admin.ModelAdmin):
  list_display =('status', 'last_status_change', 'queen_age', 'bee_type')
  list_filter=('status', 'queen_age', 'bee_type')
  search_fields=('status', 'queen_age', 'bee_type')
  
admin.site.register(Hives, HivesAdmin)

class InterventionsAdmin(admin.ModelAdmin):
  list_display=('hive', 'motif', 'date')
  list_filter=('hive', 'motif')
  search_fields=('hive', 'motif')

admin.site.register(Intervention, InterventionsAdmin)