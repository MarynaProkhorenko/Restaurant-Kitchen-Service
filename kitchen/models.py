from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class DishType(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return self.name


class Cook(AbstractUser):
    years_of_experience = models.IntegerField(default=2)

    class Meta:
        verbose_name = "cook"
        verbose_name_plural = "cooks"

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"

    def get_absolute_url(self) -> str:
        return reverse("kitchen:cook-detail", kwargs={"pk": self.pk})


class Ingredient(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}(made in {self.country})"


class Dish(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    dish_type = models.ForeignKey(DishType, on_delete=models.CASCADE)
    ingredients = models.ManyToManyField(Ingredient, related_name="dishes")
    cooks = models.ManyToManyField(Cook, related_name="dishes")

    class Meta:
        verbose_name = "dish"
        verbose_name_plural = "dishes"

    def __str__(self) -> str:
        return f"{self.name}( {self.dish_type}) costs {self.price}"

    def get_absolute_url(self) -> str:
        return reverse("kitchen:dish-detail", kwargs={"pk": self.pk})
