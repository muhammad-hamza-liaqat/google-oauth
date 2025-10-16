from django.urls import path
from .views import GoogleAuthInitView, GoogleAuthCallbackView

urlpatterns = [
    path("google/", GoogleAuthInitView.as_view(), name="google_auth"),
    path("google/callback/", GoogleAuthCallbackView.as_view(), name="google_callback"),
]
