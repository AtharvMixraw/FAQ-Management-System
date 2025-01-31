from django.contrib import admin
from .models import FAQ

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question", "created_at")
    search_fields = ("question", "question_hi", "question_bn")
    list_filter = ("created_at",)

admin.site.site_header = "FAQ Management"
admin.site.site_title = "FAQ Admin"
admin.site.index_title = "Manage FAQs"
