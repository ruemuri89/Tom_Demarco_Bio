from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Work(models.Model):
    BOOK = "book"
    ARTICLE = "article"
    PAPER = "paper"
    TYPE_CHOICES = [
        (BOOK, "Book"),
        (ARTICLE, "Article"),
        (PAPER, "Paper / Report"),
    ]

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=255, blank=True)
    year_published = models.PositiveIntegerField(null=True, blank=True)
    work_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=BOOK)
    description = models.TextField()
    key_ideas = models.TextField(help_text="Summarize the core ideas and themes")
    impact = models.TextField(help_text="Describe its impact on software engineering")
    slug = models.SlugField(unique=True, blank=True)

    def get_absolute_url(self):
        return reverse("bio:work_detail", kwargs={"slug": self.slug})
    
    class Meta:
        ordering = ["year_published", "title"]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Quote(models.Model):
    text = models.TextField()
    source = models.CharField(max_length=200, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    theme = models.CharField(
        max_length=100,
        blank=True,
        help_text="e.g. measurement, peopleware, risk, productivity",
    )

    class Meta:
        ordering = ["theme", "year"]

    def __str__(self):
        return self.text[:60] + "..."


class TimelineEvent(models.Model):
    LIFE = "life"
    CAREER = "career"
    PUBLICATION = "publication"
    OTHER = "other"
    CATEGORY_CHOICES = [
        (LIFE, "Life"),
        (CAREER, "Career"),
        (PUBLICATION, "Publication"),
        (OTHER, "Other"),
    ]

    year = models.IntegerField()
    title = models.CharField(max_length=200)
    description = models.TextField()
    category = models.CharField(
        max_length=20, choices=CATEGORY_CHOICES, default=CAREER
    )
    order_in_year = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ["year", "order_in_year"]

    def __str__(self):
        return f"{self.year} - {self.title}"


class Concept(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    summary = models.TextField()
    detailed_explanation = models.TextField(blank=True)
    # used for the “Interactive Ideas Lab” pieces
    interactive_widget_key = models.CharField(
        max_length=100,
        blank=True,
        help_text="Key used by the frontend JS to hook into this concept",
    )
    category = models.CharField(
        max_length=100,
        blank=True,
        help_text="e.g. peopleware, measurement, risk, productivity",
    )

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Influence(models.Model):
    """
    Represents things DeMarco influenced: people, methodologies, movements.
    """

    PERSON = "person"
    BOOK = "book"
    PRACTICE = "practice"
    FIELD = "field"

    TYPE_CHOICES = [
        (PERSON, "Person"),
        (BOOK, "Book"),
        (PRACTICE, "Practice / Method"),
        (FIELD, "Field / Movement"),
    ]

    name = models.CharField(max_length=200)
    influence_type = models.CharField(max_length=20, choices=TYPE_CHOICES, default=PERSON)
    description = models.TextField()
    related_work = models.ManyToManyField(Work, blank=True)
    weight = models.PositiveIntegerField(
        default=1, help_text="Rough strength of the influence (1–10)"
    )

    class Meta:
        ordering = ["-weight", "name"]

    def __str__(self):
        return self.name
