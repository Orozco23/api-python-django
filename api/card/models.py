from django.db import models
from django.core.validators import MinValueValidator

# Card model (tasks are moved between lists on the Kanban board)
class Card(models.Model):
    title = models.CharField(max_length=255, verbose_name="Card Title")
    description = models.TextField(verbose_name="Card Description", blank=True, null=True)
    column = models.CharField(
        max_length=20,
        verbose_name="Column",
        choices=[
            ('To Do', 'To Do'),
            ('In Progress', 'In Progress'),
            ('Done', 'Done')
        ],
        default='To Do'
    )
    position = models.PositiveIntegerField(verbose_name="Position in List", validators=[MinValueValidator(1)])
    due_date = models.DateTimeField(verbose_name="Due Date", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        ordering = ['column', 'position']  # Sort cards by position in the list
    def __str__(self):
        return self.title