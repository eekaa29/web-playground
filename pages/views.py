from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Page
from django.urls import reverse_lazy
from .forms import PageForm

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
    form_class = PageForm
    success_url = reverse_lazy("pages:pages")

class PageUpdate(UpdateView):
    template_name_suffix  = "_update_form"
    model = Page
    fields = ["title", "content", "order"]
    #En caso de quere mandarlo directamente a la vista donde aparecen todas las páginas=>success_url = reverse_lazy("pages:pages")
    #Pero voy a hacerlo un poco más currado, voy a enseñar como queda el propio formulario editado, y luego dar posibilidad de ver la página ya editada en page.html

    def get_success_url(self):
        return reverse_lazy("pages:update", args=[self.object.id]) + "?ok"
    


class PageDeleteView(DeleteView):
    model = Page
    success_url = reverse_lazy("pages:pages")