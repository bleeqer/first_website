from django.db import models

class Portfolio(models.Model):
    image = models.ImageField(blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    uploadTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title