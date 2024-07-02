from django.contrib import admin
from . models import Item, Category, ItemSpecification

# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    list_filter = ("category", "available",)


admin.site.register(Item, ItemAdmin)

admin.site.register(Category)

admin.site.register(ItemSpecification)