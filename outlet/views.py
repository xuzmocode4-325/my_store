from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
from django.db.models import Min, Max


from . models import Item, Category

# Create your views here.

def index(request):
    items = Item.objects.all().order_by("-price")
    num_items = items.count()

    return render(request, "outlet/index.html", {
        "items": items,
        "item_count": num_items,
    })

def item_by_id(request, id): 
    #try:
    #   item = Item.objects.get(pk=id)
    #except:
    #    raise Http404()
    redirect_slug = Item.objects.get(pk=id).slug
    redirect_path = reverse("item", args=[redirect_slug])
    return HttpResponseRedirect(redirect_path)

    
def item(request, slug):
    item = get_object_or_404(Item, slug=slug)
    return render(request, "outlet/item.html", {
        "name": item.name,
        "description":item.description,
        "category":item.category,
        "price":item.price,
        "stock": item.stock,
        "available":item.available, 
    })