from typing import Any
from django.shortcuts import render
from .models import MenuItem
from django.views.generic import ListView, DetailView


class MenuListView(ListView):
    """
    A view to display a list of menu items.

    Attributes:
        queryset (QuerySet): The queryset to fetch menu items, ordered by date_created in descending order.
        template_name (str): The name of the template to render for the list view.
        context_object_name (str): The name of the variable to use in the template to access the list of menu items.
    """
    queryset = MenuItem.objects.order_by('-date_created')
    template_name = 'Menu/index.html'
    context_object_name = 'menu_listing'

    def get_context_data(self, **kwargs):
        """
        Adds additional context data to be used in the template.

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: Dictionary containing the context data.
        """
        context = super().get_context_data(**kwargs)
        context['menu_items'] = ['pizza', 'pasta']
        return context


class MenuItemDetail(DetailView):
    """
    A view to display details of a single menu item.

    Attributes:
        model (Model): The model class for the menu item.
        template_name (str): The name of the template to render for the detail view.
    """
    model = MenuItem
    template_name = 'Menu/menu_item_detail.html'
