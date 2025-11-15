from django.urls import path
from . import views

app_name = "bio"

urlpatterns = [
    path("test/", views.TestView.as_view(), name="test"),
    path("", views.HomeView.as_view(), name="home"),
    path("biography/", views.BiographyView.as_view(), name="biography"),

    # WORKS
    path("works/", views.WorkListView.as_view(), name="works"),
    path("works/<slug:slug>/", views.WorkDetailView.as_view(), name="work_detail"),

    path("ideas-lab/", views.IdeasLabView.as_view(), name="ideas_lab"),
    path("timeline/", views.TimelineView.as_view(), name="timeline"),
    path("legacy/", views.LegacyView.as_view(), name="legacy"),
    path("quotes/", views.QuoteListView.as_view(), name="quotes"),
]
