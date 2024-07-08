from typing import Any
from django.shortcuts import render
from .models import MenuItem, COURSE_CHOICES
from django.views.generic import ListView, DetailView, TemplateView


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
    context_object_name = 'menu_list'

    def get_context_data(self, **kwargs):
        """
        Adds additional context data to be used in the template.

        Args:
            **kwargs: Arbitrary keyword arguments.

        Returns:
            dict: Dictionary containing the context data.
        """
        context = super().get_context_data(**kwargs)
        context['courses'] = COURSE_CHOICES
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


class AboutView(TemplateView):
    """
    A view to display the about page.
    
    Attributes:
        template_name (str): The name of the template to render for the about page.
    """
    template_name = 'Menu/about.html'

    def get_context_data(self, **kwargs):
        """
        Get context data for the about page.
        """
        context = super().get_context_data(**kwargs)
        # Add custom text content to the context
        context['about_text'] = """
<!-- About Us Section -->
<section id="about">
    <h2 class="pt-5">About Us</h2><hr>
    <p>Welcome to DeliciousBite, where every meal is a culinary delight crafted with passion and expertise! At DeliciousBite, we believe that dining is not just about eating; it's about experiencing flavors that tantalize the taste buds and create lasting memories.</p>
    <p>Our restaurant is dedicated to serving you the finest dishes made from the freshest ingredients sourced locally. Each item on our menu is carefully curated to satisfy even the most discerning palate.</p>
    <p>At DeliciousBite, we're committed to providing exceptional service that goes above and beyond your expectations. Whether you're celebrating a special occasion or simply craving a delicious meal, our warm and inviting ambiance sets the perfect backdrop for any dining experience.</p>
</section>

<!-- Contact Us Section -->
<section id="contact">
    <h2 class="pt-5">Contact Us</h2><hr>
    <p>For reservations, inquiries, or feedback, please feel free to contact us via email at <a class="menu-item fw-bold" href="mailto:info@deliciousbite.com">info@deliciousbite.com</a>. Our team is available to assist you with any questions you may have and ensure that your dining experience at DeliciousBite is nothing short of exceptional. We value your feedback and are always striving to improve our services to better serve you.</p>
    <p>Thank you for choosing DeliciousBite. We can't wait to see you soon!</p>
</section>
"""
        return context