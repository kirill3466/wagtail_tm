from django.urls import path, include
from .views import LoginUser, logoutUser, RegisterUser
from wagtail import urls as wagtail_urls

urlpatterns = [
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logoutUser, name='logout'),
    path('register/', RegisterUser.as_view(), name='register'),

]


urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]