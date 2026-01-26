from django.db import models

# Create your models here.


from django.db import models

class Post(models.Model):
    DRAFT = "draft"
    ARCHIVED = "archived"
    PUBLISHED = "published"

    STATUS_CHOICES = [
        (DRAFT, "Draft"),
        (PUBLISHED, "Published"),
        (ARCHIVED, "Archived"),
    ]

    text = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default=DRAFT
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text[:50]
