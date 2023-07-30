from django.urls import path
from .views_front import (
    CookieStandCreateView,
    CookieStandDeleteView,
    CookieStandDetailView,
    CookieStandListView,
    CookieStandUpdateView,
)

app_name = 'cookie_stands'

urlpatterns = [
    path("", CookieStandListView.as_view(), name="cookie_stand_list"),
    path("<int:pk>/", CookieStandDetailView.as_view(), name="cookie_stand_detail"),
    path("create/", CookieStandCreateView.as_view(), name="cookie_stand_create"),
    path("<int:pk>/update/", CookieStandUpdateView.as_view(), name="cookie_stand_update"),
    path("<int:pk>/delete/", CookieStandDeleteView.as_view(), name="cookie_stand_delete"),
]

# u can add cookie by hitthing the full url in the browser or by using the form in the home page
# http:// localhost:8000/cookie_stands/create/
