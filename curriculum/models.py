from django.db import models


class Experience(models.Model):
    company = models.CharField(max_length=50, blank=True, null=True)
    position = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=500)
