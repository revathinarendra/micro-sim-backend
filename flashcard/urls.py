from django.urls import path
from . import views

urlpatterns = [
    path('create-prompt/', views.create_prompt, name='create-prompt'),
    path('prompts/', views.get_prompts_by_wikipedia_link, name='get_prompts_by_wikipedia_link'),
    
    path('get-code-by-wikipedia-url/',views.get_code_by_wikipedia_url,name = 'get_code_by_wikipedia_url'),
    path('wikipedia/<slug:slug>/', views.WikipediaDetailView.as_view(), name='wikipedia-detail'),

]
