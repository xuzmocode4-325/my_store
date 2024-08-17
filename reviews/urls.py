from django.urls import path
from . import views


urlpatterns = [
    path("", views.ReviewView.as_view()),  
    path(
        "thank-you", 
        views.ThankYouView.as_view(), 
        name="thank-you"
    ),
    path("all-reviews", 
        views.ReviewListView.as_view(),
        name="all-reviews"
    ),
    path("favorite", 
        views.AddFavoriteView.as_view(), 
        name="favorite"),
    path("<int:pk>/", 
        views.ReviewDetailView.as_view(), 
        name="review-detail")
]
