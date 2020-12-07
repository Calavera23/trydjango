from django.db import models
from django.urls import reverse
# Create your models here.
class Cource(models.Model):
    title=models.CharField(max_length=120)
   

    def get_absolute_url(self):
    	return reverse('cources:cource', kwargs={"pk": self.id})