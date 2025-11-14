from django.test import TestCase
from bio.models import Work


class TestWorkModel(TestCase):

    def test_str_representation(self):
        work = Work.objects.create(
            title="Sample",
            year_published=1999,
            work_type="book"
        )
        self.assertEqual(str(work), "Sample")
