from django.contrib import admin
from .models import Work, Quote, TimelineEvent, Concept, Influence


@admin.register(Work)
class WorkAdmin(admin.ModelAdmin):
    list_display = ("title", "year_published", "work_type")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "description", "key_ideas")


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ("short_text", "theme", "year", "source")
    search_fields = ("text", "theme", "source")

    def short_text(self, obj):
        return obj.text[:60] + "..."


@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ("year", "title", "category", "order_in_year")
    list_filter = ("category",)
    search_fields = ("title", "description")


@admin.register(Concept)
class ConceptAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "interactive_widget_key")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name", "summary", "detailed_explanation")


@admin.register(Influence)
class InfluenceAdmin(admin.ModelAdmin):
    list_display = ("name", "influence_type", "weight")
    list_filter = ("influence_type",)
    search_fields = ("name", "description")
    filter_horizontal = ("related_work",)
