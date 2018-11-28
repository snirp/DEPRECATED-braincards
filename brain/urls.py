from django.contrib import admin
from django.urls import include, path

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('q/',      include('questions.html.urls')),
    path('rest/',   include('questions.rest.urls')),
    path('admin/',  admin.site.urls),
]
