from django.test import TestCase
from django.shortcuts import reverse


class LeadListPageTest(TestCase):
    def test_status_code(self):
        response = self.client.get(reverse("lead-list"))
        self.assertEqual(response.status_code, 200)

    def test_template_Name(self):
        response = self.client.get(reverse("landing-page"))
        self.assertTemplateUsed(response, "landing.html")
