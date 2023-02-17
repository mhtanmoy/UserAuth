
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static
from rest_framework import permissions

from drf_yasg2.views import get_schema_view
from drf_yasg2 import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="USERAUTH API",
        default_version="v1",
        description="USERAUTH API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="", url=""),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


swagger_url = [
    path("swagger.json/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/",schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui",),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('userapp.urls')),

] + swagger_url

if settings.DEBUG:
    urlpatterns = urlpatterns + static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
    # urlpatterns = urlpatterns + static(
    #     settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    # )