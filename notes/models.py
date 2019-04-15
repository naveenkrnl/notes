from django.conf import settings
from django.db import models

# Create your models here.

class NotesData(models.Model):
    user=models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    text=models.CharField(max_length=1200,blank=True,null=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text