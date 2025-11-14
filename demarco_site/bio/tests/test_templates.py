from django.test import TestCase
from django.urls import reverse


class TestTemplateContent(TestCase):

    @classmethod
    def setUpTestData(cls):
        from bio.models import Work
        cls.work = Work.objects.create(
            title="Test Work",
            year_published=2000,
            work_type="book"
        )

    def test_biography_has_sections(self):
        response = self.client.get(reverse("bio:biography"))
        content = response.content.decode("utf-8")

        self.assertIn("Biography", content)
        self.assertIn("Core Works", content)
        self.assertIn("Core Concepts", content)
        self.assertIn("Influence & Legacy", content)

    def test_work_detail_contains_fields(self):
        response = self.client.get(reverse("bio:work_detail", args=[self.work.pk]))
        content = response.content.decode("utf-8")

        self.assertIn("Published:", content)
        self.assertIn("Test Work", content)
