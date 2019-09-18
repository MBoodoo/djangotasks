from django.db import models

# Create your models here.
class Tasks(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    complete = models.BooleanField(default=False)
    flair = models.CharField(max_length=10)


    def _str_(self):
        return self.title