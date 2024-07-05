from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Subcategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, related_name='subcategories', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        unique_together = ('name', 'category')
        verbose_name = 'subcategory'
        verbose_name_plural = 'subcategories'

    def __str__(self):
        return f"{self.name} ({self.category.name})"


class ItemType(models.Model):
    name = models.CharField(max_length=100)
    subcategory = models.ForeignKey(
        Subcategory, related_name='item_types', on_delete=models.CASCADE)
    slug = models.SlugField(max_length=50, unique=True)

    class Meta:
        unique_together = ('name', 'subcategory')

    def __str__(self):
        return f"{self.name} ({self.subcategory.name})"


class Item(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=255, unique=True, blank=True, db_index=True
    )
    description = models.TextField()
    category = models.ForeignKey(Category, 
        related_name='items', on_delete=models.CASCADE, null=True)
    subcategory = models.ForeignKey(Subcategory, 
        related_name='items', on_delete=models.CASCADE, null=True)
    item_type = models.ForeignKey(ItemType, 
        related_name='items', on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d/', blank=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'item'
        verbose_name_plural = 'items'

    def clean(self):
        from django.core.exceptions import ValidationError

        if self.subcategory.category != self.category:
            raise ValidationError(f"Subcategory '{self.subcategory}' does not belong to category '{self.category}'.")

        if self.item_type.subcategory != self.subcategory:
            raise ValidationError(f"Item type '{self.item_type}' does not belong to subcategory '{self.subcategory}'.")

    def save(self, *args, **kwargs):
        self.clean()
        super(Item, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.price})"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("item", args=[self.slug])


class Review(models.Model):
    item = models.ForeignKey(
        Item, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name='reviews', on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-created_at',)
        unique_together = ('item', 'user')

    def __str__(self):
        return f'Review by {self.user.username} on {self.item.name}'


class ItemSpecification(models.Model):
    item = models.ForeignKey(
        Item, related_name='specifications', on_delete=models.CASCADE)
    specification = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.specification}'
