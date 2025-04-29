from django.shortcuts import render, get_object_or_404
from django.views.generic.list import ListView
from registration.models import Profile
from django.views.generic.detail import DetailView
# Create your views here.

class ProfileListView(ListView):
    model = Profile
    template_name = "profiles/profile_list.html"
    paginate_by = 2

    
class ProfileDetailView(DetailView):
    model = Profile
    template_name = "profiles/profile_detail.html"

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs["username"])