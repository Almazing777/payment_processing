from django.db import models

# Create your models here.
class profile(models.Model):
    name = models.CharField(max_length = 1200)
    description = models.TextField(default="description default")
    location = models.CharField(max_length = 1200, default = "my location")

    def __unicode__(self):
        return self.name