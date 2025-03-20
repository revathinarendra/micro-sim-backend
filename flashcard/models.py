from django.db import models
from django.contrib.auth.models import User

class Prompt(models.Model):
    Prompt_title = models.CharField(max_length=255,null=True,blank=True)
    Prompt = models.TextField(null=True,blank=True)
    Wikipedia_link = models.URLField(max_length=200, blank=True, null=True)
    Code = models.TextField(blank=True, null=True)
    Summary = models.TextField(blank=True, null=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Prompt_title if self.Prompt_title else "Unnamed Prompt"
