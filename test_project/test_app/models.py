from django.core.validators import MaxLengthValidator
from django.db import models

# Create your models here.


class Article(models.Model):

    title = models.CharField(max_length=120)  # Default: maxlength 255 characters
    short_story = models.TextField(validators=[MaxLengthValidator(255)], default='')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Blog posts"


class Introduction(models.Model):

    title = models.CharField(max_length=120)
    introduction_text = models.TextField()
    template_tag = models.CharField(max_length=76, default='')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Page introductions"
