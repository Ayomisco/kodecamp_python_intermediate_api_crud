
from django.db import models

class Messages(models.Model):
    name = models.CharField(max_length=288)
    age = models.IntegerField()
    messages = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        
        return f"{self.name} - {self.created_at.strftime('%H: %M: %S')}"
        

    class Meta:
        ordering = ("-created_at",)
        verbose_name = "messages"
        verbose_name_plural = "messages" 