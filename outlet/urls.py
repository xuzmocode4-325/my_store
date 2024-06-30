from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
    path("<int:id>", views.item_by_id),
    path("<slug:slug>", views.item, name="item")
]
