from django.contrib import admin
from django.urls import include, path
from rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.github.views import GitHubOAuth2Adapter
from allauth.socialaccount.providers.twitter.views import TwitterOAuthAdapter
from rest_auth.social_serializers import TwitterLoginSerializer
from rest_auth.registration.views import SocialConnectView
from rest_auth.social_serializers import TwitterConnectSerializer
from rest_auth.registration.views import ( SocialAccountListView, SocialAccountDisconnectView )


class GithubLogin(SocialLoginView):
    adapter_class = GitHubOAuth2Adapter


class GithubConnect(SocialConnectView):
    adapter_class = GitHubOAuth2Adapter


class TwitterLogin(SocialLoginView):
    serializer_class = TwitterLoginSerializer
    adapter_class = TwitterOAuthAdapter


class TwitterConnect(SocialConnectView):
    serializer_class = TwitterConnectSerializer
    adapter_class = TwitterOAuthAdapter


urlpatterns = [
    path('q/',      include('questions.html.urls')),
    path('rest/',   include('questions.rest.urls')),
    path('admin/',  admin.site.urls),
    path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
    path('rest-auth/github/', GithubLogin.as_view(), name='github_login'),
    path('rest-auth/github/connect/', GithubConnect.as_view(), name='github_connect'),
    path('rest-auth/twitter/', TwitterLogin.as_view(), name='twitter_login'),
    path('rest-auth/twitter/connect/', TwitterConnect.as_view(), name='twitter_connect'),
    path(
        'rest-auth/socialaccounts/', 
        SocialAccountListView.as_view(), 
        name='social_account_list'
    ),
    path(
        'rest-auth/socialaccounts/<int:pk>/disconnect/',
        SocialAccountDisconnectView.as_view(),
        name='social_account_disconnect'
    ),
]
