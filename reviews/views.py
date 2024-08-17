from typing import Any
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views import View
from django.views.generic.base import TemplateView 
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, ListView

from .forms import ReviewForm
from .models import Review
# Create your views here.

class ReviewView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = "reviews/review.html"
    success_url = "/reviews/thank-you"

class ThankYouView(View):
    template_name = "reviews/thank-you.html"

class ReviewListView(ListView): 
    template_name = "reviews/all-reviews.html"
    model = Review
    context_object_name = "reviews"

class ReviewDetailView(DetailView):
    template_name = "reviews/user-review.html"
    model = Review

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        loaded_id = Review.objects.get(pk=self.kwargs["pk"])
        try:
            favorite_id = self.request.session["favorite_review"]
            context["is_favorite"] = favorite_id == str(loaded_id.pk)
            # print(self.request.session["favorite_review"])
            # print(context)
            return context
        except KeyError:
            pass  
            return context

class AddFavoriteView(View): 
    def post(self, request):
        review_id = request.POST["review_id"]
        request.session["favorite_review"] = review_id
        return HttpResponseRedirect("/reviews/" + review_id )