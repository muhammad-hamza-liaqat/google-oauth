import jwt
import requests
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views import View
from django.conf import settings


class GoogleAuthInitView(View):
    def get(self, request):
        google_auth_url = (
            "https://accounts.google.com/o/oauth2/v2/auth"
            f"?client_id={settings.GOOGLE_CLIENT_ID}"
            f"&redirect_uri={settings.GOOGLE_REDIRECT_URI}"
            f"&response_type=code"
            f"&scope=openid%20email%20profile"
            f"&access_type=offline"
            f"&prompt=select_account"
        )
        return JsonResponse({"auth_url": google_auth_url})


class GoogleAuthCallbackView(View):

    def get(self, request):
        code = request.GET.get("code")
        if not code:
            return JsonResponse({"error": "Authorization code not provided"}, status=400)

        token_url = "https://oauth2.googleapis.com/token"
        token_data = {
            "code": code,
            "client_id": settings.GOOGLE_CLIENT_ID,
            "client_secret": settings.GOOGLE_CLIENT_SECRET,
            "redirect_uri": settings.GOOGLE_REDIRECT_URI,
            "grant_type": "authorization_code",
        }

        try:
            token_response = requests.post(token_url, data=token_data)
            token_response.raise_for_status()
            token_json = token_response.json()
        except requests.exceptions.RequestException as e:
            return JsonResponse({"error": "Failed to get access token", "details": str(e)}, status=400)

        access_token = token_json.get("access_token")
        if not access_token:
            return JsonResponse({"error": "Access token not found in response"}, status=400)

        user_info = requests.get(
            "https://www.googleapis.com/oauth2/v2/userinfo",
            headers={"Authorization": f"Bearer {access_token}"}
        ).json()

        email = user_info.get("email")
        name = user_info.get("name") or email.split("@")[0]

        if not email:
            return JsonResponse({"error": "Email not provided by Google"}, status=400)

        user, created = User.objects.get_or_create(email=email, defaults={"username": name})

        payload = {"user_id": user.id, "email": user.email}
        jwt_token = jwt.encode(payload, settings.SECRET_KEY, algorithm="HS256")
        if isinstance(jwt_token, bytes):
            jwt_token = jwt_token.decode("utf-8")

        message = "User registered successfully" if created else "Login successful"

        return JsonResponse({
            "message": message,
            "user": {"email": user.email, "name": user.username},
            "jwt_token": jwt_token,
        })
