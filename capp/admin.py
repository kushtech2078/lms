from django.contrib import admin
from .models import TableName  # Import your model

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
