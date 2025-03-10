from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime

class Painting(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    author = models.CharField(max_length=255, verbose_name="Author")
    month_created = models.PositiveIntegerField(
        verbose_name="Month created",
        validators=[
            MinValueValidator(1),  # Minimum month 1 (January)
            MaxValueValidator(12)  # Maximum 12 (December)
        ]
    )
    year_created = models.PositiveIntegerField(
        verbose_name="Year created", 
        validators=[
            MinValueValidator(1),  # Minimum year allowed
            MaxValueValidator(datetime.datetime.now().year)  # Maximum year allowed (current year)
        ]
    )
    description = models.TextField(verbose_name="Description", blank=True, null=True)
    material = models.CharField(max_length=255, verbose_name="Material used")
    dimensions = models.CharField(max_length=100, verbose_name="Size (Width x Height in cm)")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Registration date")
    updated_date = models.DateTimeField(auto_now=True, verbose_name="Last update")

    class Meta:
        verbose_name = "Painting"
        verbose_name_plural = "Paintings"
        ordering = ['year_created', 'title']

    def __str__(self):
        return f"{self.title}, {self.author} ({self.year_created})"
