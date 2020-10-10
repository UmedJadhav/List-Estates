from django.db import models
from datetime import datetime

# Create your models here.
class Realtor(models.Model):
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='photos/realtors/%Y/%m/%d')
    description = models.TextField(blank=True)
    phone = models.CharField(max_length=20)
    email = models.CharField(max_length=50)
    is_mvp = models.BooleanField(default=False)
    hire_date = models.DateField(default=datetime.now, blank=True)
    

    class Meta:
        verbose_name = "Realtor"
        verbose_name_plural = "Realtors"

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse("Realtor_detail", kwargs={"pk": self.pk})
