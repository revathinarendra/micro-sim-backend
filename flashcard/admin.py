
from django.contrib import admin
from .models import Prompt
from account.admin import custom_admin_site

class PromptAdmin(admin.ModelAdmin):
    list_display = ('Prompt_title', 'User', 'created_at')
    search_fields = ('Prompt_title', 'Prompt', 'Summary')
    list_filter = ('created_at',  'User')

custom_admin_site.register(Prompt, PromptAdmin)
