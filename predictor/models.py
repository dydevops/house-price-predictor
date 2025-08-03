from django.db import models

# Create your models here.
class CSVData(models.Model):
    file = models.FileField(upload_to='ml/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Data uploaded on {self.uploaded_at.strftime('%Y-%m-%d %H:%M')}"