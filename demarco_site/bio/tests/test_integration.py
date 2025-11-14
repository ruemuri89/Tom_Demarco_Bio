from django.test import TestCase
from django.urls import reverse
from bio.models import Work


class TestSiteNavigation(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.work = Work.objects.create(
            title="Integration Test Work",
            year_published=2020,
            work_type="book"
        )

    def test_navigation_flow(self):
        # home
        response = self.client.get(reverse("bio:home"))
        self.assertEqual(response.status_code, 200)

        # works page
        response = self.client.get(reverse("bio:works"))
        self.assertContains(response, "Integration Test Work")

        # detail page
        url = reverse("bio:work_detail", args=[self.work.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Integration Test Work")

        # biography
        response = self.client.get(reverse("bio:biography"))
        self.assertEqual(response.status_code, 200)
