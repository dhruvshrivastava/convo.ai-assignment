from django.contrib.auth.views import LogoutView
from django.urls import path

from convo.views import oauth, oauth_callback, home

urlpatterns = [
    path("", oauth, {"domain": "login"}, name="oauth"),
    path("sandbox/", oauth, {"domain": "test"}, name="oauth-sandbox"),
    path("callback/", oauth_callback, name="oauth-callback"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("home", home, name="home")
]