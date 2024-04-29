from django.urls import path
from . import views


urlpatterns = [
    path(route='', view=views.MenuListView.as_view(), name='home'),
    # Defining a path for viewing details of a specific menu item, and specify the URL pattern,
    # where '<int:pk>' denotes an integer parameter called 'pk' (primary key)
    path(route='menu_item/<int:pk>/',
         view=views.MenuItemDetail.as_view(), name='menu_item_detail'),
    path(route='about/', view=views.AboutView.as_view(), name='about'),
]
