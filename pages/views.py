from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Page
from django.urls import reverse_lazy

# Create your views here.
class PageListView(ListView):
    template_name = "pages/pages.html"
    model= Page

class PageDetailView(DetailView):
    template_name = "pages/page.html"
    model = Page

class PageCreate(CreateView):
    template_name = "pages/page_create.html"
    model = Page
    fields = ["title", "content", "order"]
    success_url = reverse_lazy("pages:pages")