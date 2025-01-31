from django.db import models
from ckeditor.fields import RichTextField
from googletrans import Translator

class FAQ(models.Model):
    question = models.TextField()
    answer = RichTextField()  # WYSIWYG Editor Support

    # Translations
    question_hi = models.TextField(null=True, blank=True)  # Hindi
    question_bn = models.TextField(null=True, blank=True)  # Bengali
    question_fr = models.TextField(null=True, blank=True)  # French
    question_es = models.TextField(null=True, blank=True)  # Spanish

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_translated_question(self, lang):
        """Return the translated question based on language code."""
        return getattr(self, f"question_{lang}", self.question)
    
    def save(self, *args, **kwargs):
        """Automatically translate the question when saving."""
        translator = Translator()

        if not self.question_hi:
            self.question_hi = translator.translate(self.question, dest="hi").text
        if not self.question_bn:
            self.question_bn = translator.translate(self.question, dest="bn").text
        if not self.question_fr:
            self.question_fr = translator.translate(self.question, dest="fr").text
        if not self.question_es:
            self.question_es = translator.translate(self.question, dest="es").text

        super().save(*args, **kwargs)

    def __str__(self):
        return self.question[:50]  # Show first 50 characters
