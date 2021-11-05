from django.db import models

# Create your models here.


class Content_Article(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    created_at = models.DateField(auto_now_add=True, null=True)