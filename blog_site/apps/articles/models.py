from django.contrib.auth.models import User
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, verbose_name="user", on_delete=models.CASCADE)

    class Meta:
        indexes = [models.Index(fields=["title", "content"])]

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    def __str__(self):
        return self.name
