from django.shortcuts import render
from .models import MenuItem
from django.views.generic import ListView, DetailView


class MenuListView(ListView):
    """
    A view to display a list of menu items.

    Attributes:
        queryset (QuerySet): The queryset to fetch menu items, ordered by date_created in descending order.
        template_name (str): The name of the template to render for the list view.
    """
    queryset = MenuItem.objects.order_by('-date_created')
    template_name = 'index.html'


class MenuItemDetail(DetailView):
    """
    A view to display details of a single menu item.

    Attributes:
        model (Model): The model class for the menu item.
        template_name (str): The name of the template to render for the detail view.
    """
    model = MenuItem
    template_name = 'menu_item_detail.html'
