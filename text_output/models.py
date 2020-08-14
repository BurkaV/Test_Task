from django.db import models

class AcceptsText(models.Model):
    text = models.CharField(max_length=2000)
    small = models.JSONField()
    medium = models.JSONField()
    large = models.JSONField()
    def __str__(self):
        return self.text









