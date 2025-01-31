from rest_framework import generics
from rest_framework.response import Response
from django.core.cache import cache
from .models import FAQ
from .serializers import FAQSerializer
from django.http import JsonResponse

def api_home(request):
    return JsonResponse({"message": "Welcome to the FAQ API!"})


class FAQListView(generics.ListAPIView):
    """API to retrieve FAQs with optional language selection."""
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer

    def get(self, request, *args, **kwargs):
        lang = request.query_params.get("lang", "en")  # Default to English
        cache_key = f"faqs_{lang}"  # Cache key for this language
        cached_data = cache.get(cache_key)

        if cached_data:
            return Response(cached_data)

        # If not cached, fetch from DB and serialize
        faqs = self.get_queryset()
        serializer = self.get_serializer(faqs, many=True, context={"request": request})

        # Store response in cache
        cache.set(cache_key, serializer.data, timeout=3600)  # Cache for 1 hour
        return Response(serializer.data)
