from django.db import models
from django.contrib.auth.models import User
from urllib.parse import urlparse

class Prompt(models.Model):
    Prompt_title = models.CharField(max_length=255,null=True,blank=True)
    Prompt = models.TextField(null=True,blank=True)
    Wikipedia_link = models.URLField(max_length=200, blank=True, null=True)
    Code = models.JSONField(blank=True, null=True)
    Summary = models.TextField(blank=True, null=True)
    User = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    mcq = models.JSONField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return self.Prompt_title if self.Prompt_title else "Unnamed Prompt"
def extract_slug(url):
    try:
        return urlparse(url).path.strip('/').split('/')[-1]
    except:
        return None
    
class Wikipedia(models.Model):
    wikipedia_url = models.URLField(max_length=200, blank=True, null=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True) 
    mermaid_Code = models.TextField(blank=True, null=True)
    p5_code = models.TextField(blank=True, null=True)
    three_Code = models.TextField(blank=True, null=True)
    d3_code = models.TextField(blank=True, null=True)
    code_avaliable = models.BooleanField(default=False)

    def extract_slug(self):
            try:
                return urlparse(self.wikipedia_url).path.strip('/').split('/')[-1]
            except:
                return None

    def save(self, *args, **kwargs):
        if self.wikipedia_url and not self.slug:
            self.slug = self.extract_slug()
        self.code_avaliable = any([self.mermaid_Code, self.p5_code, self.three_Code, self.d3_code])
        super().save(*args, **kwargs)
    

    def __str__(self):
        return self.wikipedia_url or  "No url"