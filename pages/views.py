from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Page

# Create your views here.
class PageListView(ListView):
    template_name = "pages/pages.html"
    model= Page

class PageDetailView(DetailView):
    template_name = "pages/page.html"
    model = Page