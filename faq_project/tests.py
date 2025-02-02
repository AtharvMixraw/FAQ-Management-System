from django.test import TestCase
from django.urls import reverse
from faq_project.models import FAQ
from rest_framework.test import APIClient


class FAQModelTest(TestCase):
    """Test cases for FAQ model"""

    def setUp(self):
        """Create a test FAQ object before each test."""
        self.faq = FAQ.objects.create(
            question="What is Django?",
            answer="Django is a Python-based web framework.",
            question_hi="Django क्या है?",
            question_bn="Django কি?",
            question_fr="Qu'est-ce que Django?",
            question_es="¿Qué es Django?"
        )

    def test_faq_creation(self):
        """Test if an FAQ object is created correctly."""
        self.assertEqual(self.faq.question, "What is Django?")
        self.assertEqual(self.faq.answer, "Django is a Python-based web framework.")

    def test_faq_str(self):
        """Test if the __str__ method returns the question."""
        self.assertEqual(str(self.faq), "What is Django?")


class FAQAPITest(TestCase):
    """Test cases for FAQ API"""

    def setUp(self):
        """Setup test data and API client"""
        self.client = APIClient()
        self.faq = FAQ.objects.create(
            question="How does caching work?",
            answer="Caching stores frequently accessed data.",
            question_hi="कैशिंग कैसे काम करता है?",
            question_bn="ক্যাশিং কিভাবে কাজ করে?",
            question_fr="Comment fonctionne la mise en cache?",
            question_es="¿Cómo funciona el almacenamiento en caché?"
        )

    def test_api_home(self):
        """Test if the API home endpoint returns a success response."""
        response = self.client.get(reverse("api-home"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Welcome to the FAQ API!"})

    def test_api_faq_list(self):
        """Test if the FAQ list API returns FAQs."""
        response = self.client.get(reverse("faq-list"))
        self.assertEqual(response.status_code, 200)
        self.assertGreater(len(response.json()), 0)

    def test_api_faq_list_with_language(self):
        """Test if the API returns translated questions when language is specified."""
        response = self.client.get(reverse("faq-list") + "?lang=fr")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Comment fonctionne la mise en cache?", str(response.json()))
