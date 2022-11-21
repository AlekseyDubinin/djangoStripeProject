from django.db import models

# Django Модель Item с полями (name, description, price)


class Item(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, null=True)
    price = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name
