from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialAccount
from django.contrib.auth import get_user_model
from django.utils.text import slugify
import random

User = get_user_model()

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def populate_user(self, request, sociallogin, data):
        """Auto-populate username from Google email before @ and ensure uniqueness."""
        user = sociallogin.user
        google_email = data.get("email")

        if google_email:
            user.email = google_email
            base_username = google_email.split("@")[0]
            user.username = self.generate_unique_username(base_username)
        else:
            user.username = f"user{random.randint(1000, 9999)}"
        
        user.is_active = True
        if not user.password:
            user.set_unusable_password()
        return user

    def generate_unique_username(self, base_username):
        """Ensure unique username by appending random digits if needed."""
        new_username = slugify(base_username)
        if User.objects.filter(username=new_username).exists():
            while True:
                random_suffix = random.randint(1000, 9999)
                unique_username = f"{new_username}{random_suffix}"
                if not User.objects.filter(username=unique_username).exists():
                    return unique_username
        return new_username

    def pre_social_login(self, request, sociallogin):
        """Auto-link Google account to existing user and prevent signup form."""
        if sociallogin.is_existing:
            return  # User is already linked, continue login

        # Check if user already exists with the same email
        email = sociallogin.account.extra_data.get('email')
        if email:
            try:
                user = User.objects.get(email=email)
                sociallogin.connect(request, user)  # Auto-link without signup page
            except User.DoesNotExist:
                pass  # Allow normal signup for new users

class MyAccountAdapter(DefaultAccountAdapter):
    def is_open_for_signup(self, request):
        return True
