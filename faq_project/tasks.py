from celery import shared_task
from googletrans import Translator
from .models import FAQ

@shared_task
def translate_faq(faq_id):
    """Background task to translate FAQ question."""
    faq = FAQ.objects.get(id=faq_id)
    translator = Translator()

    faq.question_hi = translator.translate(faq.question, dest="hi").text
    faq.question_bn = translator.translate(faq.question, dest="bn").text
    faq.question_fr = translator.translate(faq.question, dest="fr").text
    faq.question_es = translator.translate(faq.question, dest="es").text

    faq.save()
    return f"Translated FAQ {faq_id}"
