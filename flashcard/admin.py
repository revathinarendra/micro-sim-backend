
from django.contrib import admin
from .models import Prompt,Wikipedia
from accounts.admin import custom_admin_site


class PromptAdmin(admin.ModelAdmin):
    list_display = ('Prompt_title', 'User', 'mcq','created_at')
    search_fields = ('Prompt_title', 'Prompt', 'Summary')
    list_filter = ('created_at',  'User')

custom_admin_site.register(Prompt, PromptAdmin)


class WikipediaAdmin(admin.ModelAdmin):
    list_display = ('wikipedia_url','slug','mermaid_Code', 'p5_code','three_Code','d3_code','summary','mcq','code_avaliable','remix1','remix2','remix3')
    search_fields = ('wikipedia_url',)

custom_admin_site.register(Wikipedia, WikipediaAdmin)


