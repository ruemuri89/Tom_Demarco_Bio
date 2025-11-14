from django.test import TestCase
from django.urls import reverse
from bio.models import Work, Concept, Quote, TimelineEvent, Influence


class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.work = Work.objects.create(
            title="Test Work",
            year_published=2000,
            work_type="book",
            description="A test description"
        )

        cls.quote = Quote.objects.create(
            text="Test Quote",
            year=2000,
            theme="test"
        )

        cls.event = TimelineEvent.objects.create(
            year=1990,
            title="Test Event",
            description="X",
            category="test",
            order_in_year=1
        )

        cls.concept = Concept.objects.create(
            name="Test Concept",
            slug="test-concept",
            summary="Summary",
            detailed_explanation="Details"
        )

        cls.influence = Influence.objects.create(
            name="Test Influence",
            influence_type="person",
            weight=5
        )

    def test_home_view(self):
        response = self.client.get(reverse("bio:home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bio/home.html")
        self.assertIn("highlight_quotes", response.context)
        self.assertIn("featured_works", response.context)

    def test_biography_view(self):
        response = self.client.get(reverse("bio:biography"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bio/biography.html")
        self.assertIn("works", response.context)
        self.assertIn("concepts", response.context)
        self.assertIn("influences", response.context)
        self.assertIn("quotes", response.context)

    def test_work_list_view(self):
        response = self.client.get(reverse("bio:works"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bio/works.html")

    def test_work_detail_view(self):
        url = reverse("bio:work_detail", args=[self.work.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bio/work_detail.html")
        self.assertEqual(response.context["work"].title, "Test Work")

    def test_ideas_lab_view(self):
        response = self.client.get(reverse("bio:ideas_lab"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bio/ideas_lab.html")
        self.assertIn("concepts", response.context)

    def test_timeline_view(self):
        response = self.client.get(reverse("bio:timeline"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "bio/timeline.html")
        self.assertIn("events", response.context)

    def test_legacy_view(self):
        response = self.client.get(reverse("bio:legacy"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("influences", response.context)
        self.assertIn("works", response.context)
