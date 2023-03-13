from django.db import models
from django.utils.translation import get_language

class Category(models.Model):
    name_en = models.CharField(max_length=255)
    name_uz = models.CharField(max_length=255)

    @property
    def name(self):
        return getattr(self, f'name_{get_language()}')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
