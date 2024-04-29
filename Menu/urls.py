from django.urls import path
from . import views


urlpatterns = [
    path(route='', view=views.MenuListView.as_view(), name='home'),
    # path(route='menu-item/', view=views.MenuItemDetail.as_view(), name='menu_item_detail'),
]