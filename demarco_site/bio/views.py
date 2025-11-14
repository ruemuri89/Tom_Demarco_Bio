from django.views.generic import TemplateView, ListView, DetailView
from .models import Work, Quote, TimelineEvent, Concept, Influence


class HomeView(TemplateView):
    template_name = "bio/home.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["highlight_quotes"] = Quote.objects.all()[:3]
        ctx["featured_works"] = Work.objects.all()[:3]
        ctx["timeline_events"] = TimelineEvent.objects.all()[:5]
        return ctx


class BiographyView(TemplateView):
    template_name = "bio/biography.html"


class WorkListView(ListView):
    model = Work
    template_name = "bio/works.html"
    context_object_name = "works"


class WorkDetailView(DetailView):
    model = Work
    template_name = "bio/work_detail.html"
    context_object_name = "work"


class IdeasLabView(TemplateView):
    """
    This is where we’ll later wire in the interactive simulators
    (team productivity, cost of delay, measurement fallacies, etc.)
    via JS widgets that read the Concept models.
    """
    template_name = "bio/ideas_lab.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["concepts"] = Concept.objects.all()
        return ctx


class TimelineView(TemplateView):
    template_name = "bio/timeline.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["events"] = TimelineEvent.objects.all()
        return ctx


class LegacyView(TemplateView):
    template_name = "bio/legacy.html"

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["influences"] = Influence.objects.all()
        ctx["works"] = Work.objects.all()
        return ctx


class QuoteListView(ListView):
    model = Quote
    template_name = "bio/quotes.html"
    context_object_name = "quotes"
