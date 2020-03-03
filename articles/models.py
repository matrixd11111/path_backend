from django.db import models
from django.utils import timezone


class SectionModel(models.Model):
    title = models.CharField(max_length=100)
    pablish = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ThemeModel(models.Model):
    section = models.ForeignKey(SectionModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    pablish = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class PablicationModel(models.Model):
    theme = models.ForeignKey(ThemeModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, null=True)
    content = models.TextField(blank=True)
    image_content = models.ImageField(upload_to='media', blank=True)
    pablish = models.DateTimeField(default=timezone.now)
    create = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=250)

    def __str__(self):
        return self.title
