from django.db import models
from ckeditor.fields import RichTextField

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()

    # Translated fields
    question_hi = models.TextField(null=True, blank=True)  # Hindi
    question_bn = models.TextField(null=True, blank=True)  # Bengali
    question_fr = models.TextField(null=True, blank=True)  # French
    question_es = models.TextField(null=True, blank=True)  # Spanish

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_translated_question(self, lang):
        return getattr(self, f"question_{lang}", self.question)

    def save(self, *args, **kwargs):
        """Save first, then trigger translation asynchronously"""
        super().save(*args, **kwargs)

        # Import Celery task inside method to avoid circular import
        from faq_project.tasks import translate_faq  
        translate_faq.delay(self.id)

    def __str__(self):
        return self.question[:50]
