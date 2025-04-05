from django.urls import path
from . import views
from .views import  save_wikipedia

urlpatterns = [
    # post to save prompt and response to the data base
    path('create-prompt/', views.create_prompt, name='create-prompt'),
    path('prompts/', views.get_prompts_by_wikipedia_link, name='get_prompts_by_wikipedia_link'),
    # get all avaliable wikipedia table
    path('get-code-by-wikipedia-url/',views.get_code_by_wikipedia_url,name = 'get_code_by_wikipedia_url'),
    # get wikipedia details
    path('wikipedia/<slug:slug>/', views.WikipediaDetailView.as_view(), name='wikipedia-detail'),
    # post from the frontend to save wikipedia table
    path('wiki/save/', save_wikipedia, name='save_wikipedia_data_alt'),
    
    

]
