from django.db import models
from django.contrib.auth.models import User


# Constants defining meal types and their labels
COURSE_CHOICES = (
    # Appetizers or small dishes served before the main course
    ("starters", "Starters"),
    ("salads", "Salads"),        # Various types of salads
    ("main_dishes", "Main Dishes"),  # Main courses or entrees
    ("desserts", "Desserts")     # Sweet dishes served after the main course
)

# Constants defining status options and their labels
STATUS_CHOICES = (
    (0, "Unavailable"),  # The menu item is not available
    (1, "Available")     # The menu item is available
)


class Menu(models.Model):
    """
    Model representing a menu item in a restaurant.

    Attributes:
        meal (str): Name of the menu item.
        description (str): Description of the menu item.
        price (Decimal): Price of the menu item.
        course (str): Course of the menu item (e.g., appetizer, main course, dessert).
        chef (User): Chef or creator of the menu item.
        status (int): Availability status of the menu item.
        date_created (DateTime): Date and time when the menu item was created.
        date_modified (DateTime): Date and time when the menu item was last modified.
    """

    meal = models.CharField(max_length=80, unique=True)
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    course = models.CharField(max_length=200, choices=COURSE_CHOICES)
    chef = models.ForeignKey(User, on_delete=models.PROTECT)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        Return a string representation of the menu item.
        """
        return self.meal
