from django.contrib import admin
from .models import TableName, DeviceTracking  # Import your model

@admin.register(TableName)
class TableNameAdmin(admin.ModelAdmin):
    list_display = ('question', 'created_at')  # Columns to display in the admin list view
    search_fields = ('question',)  # Add a search bar for the "question" field
    list_filter = ('created_at',)  # Add filters for "created_at"

    # Optional: Customize the form display
    fieldsets = (
        (None, {
            'fields': ('question', 'answer')  # Fields displayed in the admin form
        }),
        ('Metadata', {
            'fields': ('created_at',),
            'classes': ('collapse',),  # Collapsible section for metadata
        }),
    )
    readonly_fields = ('created_at',)  # Make created_at read-only

class DeviceTrackingAdmin(admin.ModelAdmin):
    # Display fields in the list view (order of columns)
    list_display = ('id', 'ip_address', 'mac_address', 'created_at')
    
    # Fields to make searchable in the admin
    search_fields = ['ip_address', 'mac_address']
    
    # Filters to use in the sidebar
    list_filter = ['created_at']
    
    # Enable sorting by created_at (default: descending order)
    ordering = ['-created_at']  # Negative sign for descending order
    
    # Optionally, you can add pagination and control the number of items per page
    list_per_page = 20  # Display 20 records per page

# Register the custom admin class for DeviceTracking
admin.site.register(DeviceTracking, DeviceTrackingAdmin)