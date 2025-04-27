from django.urls import path
from spice.views import home

urlpatterns = [
    # path(url, view function, name of url)
    path('', home, name="Homepage"),
]