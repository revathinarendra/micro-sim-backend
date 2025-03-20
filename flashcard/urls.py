from django.urls import path
from . import views

urlpatterns = [
    path('create-prompt/', views.create_prompt, name='create-prompt'),
    path('prompts/', views.get_prompts_by_wikipedia_link, name='get_prompts_by_wikipedia_link'),
    


]
