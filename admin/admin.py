from django.contrib import admin
from .models import Ramen

# Register your models here.
admin.site.register(Ramen)


class Ramen(models.Model):
    INGREDIENT_CHOICES = (
        (1, "Egg"),
        (2, "Chicken"),
        (3, "Pork"),
    )
    
    SIDE_DISH_CHOICES = (
        (1, "Pork dumpling"),
        (2, "Beef dumpling"),
    )
    
    SOUP_CHOICES = (
        (1, "Beef soup"),
        (2, "Pork soup"),
    )
    
    NOODLE_CHOICES = (
        (1, "One"),
        (2, "Two"),
    )
      
    price = models.DecimalField(max_digits=5, decimal_places=2, default=10.00)  # 22.12
    description = models.TextField()
    ingredient_choice = models.IntegerField(choices=INGREDIENT_CHOICES, default=1)
    side_dish = models.IntegerField(choices=SIDE_DISH_CHOICES, default=1)
    soup_choice = models.IntegerField(choices=SOUP_CHOICES, default=1)
    noodle_choice = models.IntegerField(choices=NOODLE_CHOICES, default=1)
      
    def __str__(self) -> str:
        return "RAMEN"
    
    def save(self, *args, **kwargs):
        if self.ingredient_choice == 1:
            self.price = decimal.Decimal(12)
        if self.ingredient_choice == 2:
            self.price = decimal.Decimal(13)
        if self.ingredient_choice == 3:
            self.price = decimal.Decimal(14)
        super(Ramen, self).save(*args, **kwargs)
