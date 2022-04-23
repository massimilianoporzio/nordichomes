from django.db import models
from nordichomes.decorators import autoslug
# Create your models here.


@autoslug("name")
class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)

    class Meta:
        ordering=('name',)
        verbose_name_plural = "categories"

    def __str__(self):
        return self.slug


@autoslug("name")
class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField(blank=True)
    description = models.TextField(blank=True,null=True)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.name