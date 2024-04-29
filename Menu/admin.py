from django.contrib import admin
from .models import MenuItem


class MenuItemAdmin(admin.ModelAdmin):
    """
    Admin configuration for the MenuItem model.

    Attributes:
        list_display (tuple): Specifies the fields to display in the list view of MenuItem objects.
        list_filter (tuple): Specifies the fields to use for filtering in the admin list view.
        search_fields (tuple): Specifies the fields to use for searching in the admin list view.
    """
    list_display = ('meal', 'status')  # display 'meal' and 'status' fields
    list_filter = ("status",)  # filter by the 'status' field
    # search using the fields 'meal' and 'description'
    search_fields = ("meal", "description")


# Register the MenuItem model with its corresponding admin configuration
admin.site.register(MenuItem, MenuItemAdmin)
