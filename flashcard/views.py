from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Prompt,Wikipedia
from .serializers import PromptSerializer,WikipediaSerializer
from django.contrib.auth.models import User
from urllib.parse import unquote
from django.contrib.auth import get_user_model


# @api_view(['POST'])
# def create_prompt(request):
#     if request.method == 'POST':
#         data = request.data

#         # Retrieve the user based on the provided email
#         user_email = data.get('User')
#         if user_email:
#             try:
#                 user = User.objects.get(email=user_email)
#             except User.DoesNotExist:
#                 return Response({'error': 'User with this email does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
#         else:
#             return Response({'error': 'User email is required.'}, status=status.HTTP_400_BAD_REQUEST)

#         # Associate the prompt with the retrieved user
#         data['User'] = user.pk

#         serializer = PromptSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({
#                 'message': 'Prompt created successfully.'
#             }, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     return Response({'error': 'Invalid request method.'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)




User = get_user_model() 


@api_view(['POST'])
def create_prompt(request):
    prompt_title = request.data.get('Prompt_title', None)
    prompt_text = request.data.get('Prompt', None)  # User-entered text prompt
    wikipedia_url = request.data.get('Wikipedia_link', None)
    
    # Ensure at least one of Wikipedia_link or Prompt is provided
    if not wikipedia_url and not prompt_text:
        return Response({"error": "At least one of Wikipedia_link or Prompt is required"}, status=status.HTTP_400_BAD_REQUEST)

    # Create and save the prompt instance
    prompt_instance = Prompt.objects.create(
        Prompt_title=prompt_title,
        Prompt=prompt_text,
        Wikipedia_link=wikipedia_url,
        User=request.user if request.user.is_authenticated else None
    )

    return Response({"message": "Prompt saved", "id": prompt_instance.id}, status=status.HTTP_201_CREATED)


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
    wikipedia_urls = Wikipedia.objects.all()
    serializer = WikipediaSerializer(wikipedia_urls,many=True)
    return Response(serializer.data)