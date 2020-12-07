from django.db import models
from django.urls import reverse
# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=120)
    content=models.TextField(blank=True,null=True)
    active=models.BooleanField(blank=True)

    def get_absolute_url(self):
    	return reverse('articles:article', kwargs={"pk": self.id})