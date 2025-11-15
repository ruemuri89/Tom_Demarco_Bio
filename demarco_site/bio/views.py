from django.views.generic import TemplateView, ListView, DetailView
from .models import Work, Quote, TimelineEvent, Concept, Influence


class HomeView(TemplateView):
    template_name = "bio/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["highlight_quotes"] = Quote.objects.all()[:3]
        ctx["featured_works"] = Work.objects.all()[:3]
        ctx["timeline_events"] = TimelineEvent.objects.order_by("year", "order_in_year")[:5]
        return ctx


class BiographyView(TemplateView):
    template_name = "bio/biography.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["works"] = Work.objects.order_by("year_published", "title")
        ctx["concepts"] = Concept.objects.order_by("name")
        ctx["influences"] = Influence.objects.order_by("-weight", "name")
        ctx["quotes"] = Quote.objects.order_by("year")
        return ctx


class WorkListView(ListView):
    model = Work
    template_name = "bio/works.html"
    context_object_name = "works"
    paginate_by = 12  # optional, but recommended for long lists
    ordering = ["year_published", "title"]
 
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["total_works"] = Work.objects.count()
        ctx["current_type"] = self.request.GET.get("type", "")
        ctx["query"] = self.request.GET.get("q", "")
        ctx["type_choices"] = Work.TYPE_CHOICES
        return ctx



class WorkDetailView(DetailView):
    model = Work
    template_name = "bio/work_detail.html"
    context_object_name = "work"
    slug_field = "slug"
    slug_url_kwarg = "slug"


class IdeasLabView(TemplateView):
    template_name = "bio/ideas_lab.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["concepts"] = Concept.objects.order_by("name")
        return ctx


class TimelineView(TemplateView):
    template_name = "bio/timeline.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["events"] = TimelineEvent.objects.order_by("year", "order_in_year")
        return ctx


class LegacyView(TemplateView):
    template_name = "bio/legacy.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["influences"] = Influence.objects.order_by("-weight", "name")
        ctx["works"] = Work.objects.order_by("year_published", "title")
        return ctx

class QuoteListView(ListView):
    model = Quote
    template_name = "bio/quotes.html"
    context_object_name = "quotes"
    ordering = ["year"]
