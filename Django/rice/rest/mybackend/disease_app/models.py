from django.db import models

# Create your models here.
class Prediction(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    detected_disease = models.CharField(max_length=255)
    average_confidence = models.FloatField()
    pesticides = models.TextField(blank=True, null=True)
    precautions = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.detected_disease} - {self.timestamp}"