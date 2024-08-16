from django.shortcuts import render
from django.views import View
from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from .forms import ProfileForm
from .models import UserProfile

# Create your views here.

class CreateProfileView(FormView):
    model = UserProfile
    form_class = ProfileForm
    template_name = "profiles/index.html"
    success_url = "/profiles/"

class ProfilesView(ListView):
    model = UserProfile
    template_name = "profiles/user-profiles.html"
    context_object_name = "profiles"

