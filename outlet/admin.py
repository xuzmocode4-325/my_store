from django import forms
from django.contrib import admin
from .models import Item, Category, ItemSpecification, Subcategory, ItemType

# Register your models here.

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ItemForm, self).__init__(*args, **kwargs)
        self.fields['subcategory'].queryset = Subcategory.objects.none()
        self.fields['item_type'].queryset = ItemType.objects.none()

        if 'category' in self.data:
            try:
                category_id = int(self.data.get('category'))
                self.fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['subcategory'].queryset = self.instance.category.subcategories

        if 'subcategory' in self.data:
            try:
                subcategory_id = int(self.data.get('subcategory'))
                self.fields['item_type'].queryset = ItemType.objects.filter(subcategory_id=subcategory_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['item_type'].queryset = self.instance.subcategory.item_types

        self.fields['subcategory'].widget.attrs.update({'data-category-id': lambda sub: sub.category_id for sub in self.fields['subcategory'].queryset})
        self.fields['item_type'].widget.attrs.update({'data-subcategory-id': lambda it: it.subcategory_id for it in self.fields['item_type'].queryset})


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']
    prepopulated_fields = {"slug": ("name",)}


class SubcategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'category']
    search_fields = ['name']
    list_filter = ['category']
    prepopulated_fields = {"slug": ("name",)}


class ItemTypeAdmin(admin.ModelAdmin):
    list_display = ['name', 'subcategory']
    search_fields = ['name']
    list_filter = ['subcategory']
    prepopulated_fields = {"slug": ("name",)}


class ItemAdmin(admin.ModelAdmin):
    form = ItemForm
    prepopulated_fields = {"slug": ("name",)}
    list_display = ['name', 'category', 'subcategory', 'item_type', 'price', 'available']
    search_fields = ['name']
    list_filter = ['category', 'subcategory', 'item_type', 'available']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields['subcategory'].queryset = Subcategory.objects.none()
        form.base_fields['item_type'].queryset = ItemType.objects.none()

        if request.method == 'GET':
            if 'category' in request.GET:
                try:
                    category_id = int(request.GET.get('category'))
                    form.base_fields['subcategory'].queryset = Subcategory.objects.filter(category_id=category_id)
                except (ValueError, TypeError):
                    pass

            if 'subcategory' in request.GET:
                try:
                    subcategory_id = int(request.GET.get('subcategory'))
                    form.base_fields['item_type'].queryset = ItemType.objects.filter(subcategory_id=subcategory_id)
                except (ValueError, TypeError):
                    pass

        elif obj is not None:
            form.base_fields['subcategory'].queryset = Subcategory.objects.filter(category=obj.category)
            form.base_fields['item_type'].queryset = ItemType.objects.filter(subcategory=obj.subcategory)

        return form
    class Media:
        js = ('outlet/admin/js/admin-filter.js',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Subcategory, SubcategoryAdmin)
admin.site.register(ItemType, ItemTypeAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(ItemSpecification)
