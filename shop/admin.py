from django.contrib import admin
from .models import *

admin.site.register(Car)
admin.site.register(Category)
admin.site.register(Company)
admin.site.register(Order)
admin.site.register(CarImages)


@admin.register(SiteContent)
class SiteContentAdmin(admin.ModelAdmin):
    list_display = ('current_text', 'original_text')  # Display these fields in the list view
    readonly_fields = ('original_text',)  # Prevent modification of the original text
    search_fields = ('original_text', 'current_text')  # Allow searching by both original and current text

    fieldsets = (
        (None, {
            'fields': ('original_text', 'current_text'),
        }),
    )

    def get_readonly_fields(self, request, obj=None):
        if obj:  # Editing an existing object
            return self.readonly_fields + ('original_text',)
        return self.readonly_fields

