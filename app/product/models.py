from django.db import models

# from ..utils.models import BaseModel

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=255)
    child = models.ManyToManyField(
        'self',
        blank=True
    )
    slug = models.SlugField(
        unique=True,
        null=True,
        blank=True
    )
    is_parent = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
