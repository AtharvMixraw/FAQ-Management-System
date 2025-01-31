from django.urls import path
from .views import FAQListView, api_home

urlpatterns = [
    path("", api_home, name="api-home"),
    path("faqs/", FAQListView.as_view(), name="faq-list"),
]
