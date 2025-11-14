from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bio.views import (
    HomeView, BiographyView, WorkListView, WorkDetailView,
    IdeasLabView, TimelineView, LegacyView, QuoteListView
)

class TestURLResolution(SimpleTestCase):

    def test_home_url(self):
        url = reverse("bio:home")
        self.assertEqual(resolve(url).func.view_class, HomeView)

    def test_biography_url(self):
        url = reverse("bio:biography")
        self.assertEqual(resolve(url).func.view_class, BiographyView)

    def test_works_list_url(self):
        url = reverse("bio:works")
        self.assertEqual(resolve(url).func.view_class, WorkListView)

    def test_ideas_lab_url(self):
        url = reverse("bio:ideas_lab")
        self.assertEqual(resolve(url).func.view_class, IdeasLabView)

    def test_timeline_url(self):
        url = reverse("bio:timeline")
        self.assertEqual(resolve(url).func.view_class, TimelineView)

    def test_legacy_url(self):
        url = reverse("bio:legacy")
        self.assertEqual(resolve(url).func.view_class, LegacyView)

    def test_quotes_url(self):
        url = reverse("bio:quotes")
        self.assertEqual(resolve(url).func.view_class, QuoteListView)
