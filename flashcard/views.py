from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Prompt,Wikipedia
from .serializers import PromptSerializer,WikipediaSerializer
from django.contrib.auth.models import User
from urllib.parse import unquote
from django.contrib.auth import get_user_model
import base64
from rest_framework.generics import RetrieveAPIView
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from django.utils.text import slugify
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

User = get_user_model() 

@api_view(['POST'])
def create_prompt(request):
    serializer = PromptSerializer(data=request.data)

    if serializer.is_valid():
        prompt_instance = serializer.save(User=request.user if request.user.is_authenticated else None)
        return Response({"message": "Prompt saved", "id": prompt_instance.id}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_prompts_by_wikipedia_link(request):
    wikipedia_link = request.query_params.get('wikipedia_link', None)
    if wikipedia_link is not None:
        wikipedia_link = wikipedia_link.strip()  # Remove leading/trailing whitespace
        wikipedia_link = unquote(wikipedia_link)  # Decode URL-encoded characters
        prompts = Prompt.objects.filter(Wikipedia_link=wikipedia_link)
        if not prompts:
            return Response({"error": "No prompts found for the given Wikipedia_link"}, status=status.HTTP_404_NOT_FOUND)
        serializer = PromptSerializer(prompts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response({"error": "Wikipedia_link parameter is required"}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def get_code_by_wikipedia_url(request):
    wikipedia_entries = Wikipedia.objects.all()
    serializer = WikipediaSerializer(wikipedia_entries, many=True)
    return Response(serializer.data)


# get the details of wikipedia urls
class WikipediaDetailView(RetrieveAPIView):
    queryset = Wikipedia.objects.all()
    serializer_class = WikipediaSerializer
    lookup_field = 'slug'

# post method to save the front data to the wikipedia table

@api_view(['POST'])
def save_wikipedia(request):
    wikipedia_url_data = request.data.get("wikipedia_url")

    # Case where frontend sends it as {"url": "https://en.wikipedia.org/xyz"}
    if isinstance(wikipedia_url_data, dict):
        wikipedia_url = wikipedia_url_data.get("url")
    else:
        wikipedia_url = wikipedia_url_data

    if not wikipedia_url or not isinstance(wikipedia_url, str):
        return Response({"error": "Invalid or missing wikipedia_url."}, status=status.HTTP_400_BAD_REQUEST)

    # Try getting an existing object
    wikipedia_obj = Wikipedia.objects.filter(wikipedia_url=wikipedia_url).first()

    if wikipedia_obj:
        serializer = WikipediaSerializer(wikipedia_obj, data=request.data, partial=True)
    else:
        if 'slug' not in request.data or not request.data['slug']:
            request.data['slug'] = slugify(wikipedia_url.split('/')[-1])
        request.data['wikipedia_url'] = wikipedia_url  # Make sure it's the cleaned string
        serializer = WikipediaSerializer(data=request.data)

    if serializer.is_valid():
        wikipedia_instance = serializer.save()
        return Response({
            "message": "Wikipedia entry saved", 
            "id": wikipedia_instance.id,
            "data": serializer.data
        }, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WikipediaUpdateOrCreateView(APIView):
    def put(self, request, remix_field, *args, **kwargs):
        # Extract the Wikipedia URL
        wikipedia_url = request.data.get("wikipedia_url")
        if not wikipedia_url:
            return Response({"error": "Wikipedia URL is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Check if the remix_field is valid (remix1, remix2, remix3)
        if remix_field not in ['remix1', 'remix2', 'remix3','mcq_content']:
            return Response({"error": "Invalid remix field."}, status=status.HTTP_400_BAD_REQUEST)

        # Build the defaults dictionary dynamically based on the remix_field
        remix_data = request.data.get(remix_field)
        if not remix_data:
            return Response({"error": f"{remix_field} data is required."}, status=status.HTTP_400_BAD_REQUEST)

        # Prepare the defaults to update the selected remix field
        defaults = {remix_field: remix_data}

        # Update or create the Wikipedia entry
        obj, created = Wikipedia.objects.update_or_create(
            wikipedia_url=wikipedia_url,
            defaults=defaults
        )

        # Serialize the updated or created object
        serializer = WikipediaSerializer(obj)
        return Response(serializer.data, status=status.HTTP_201_CREATED if created else status.HTTP_200_OK)
