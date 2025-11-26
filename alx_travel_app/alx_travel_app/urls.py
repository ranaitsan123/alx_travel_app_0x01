from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="ALX Travel API",
        default_version='v1',
        description="CRUD API for Listings and Bookings",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path("admin/", admin.site.urls),

    # API routes using DRF router
    path("api/", include("listings.urls")),

    # Swagger documentation
    path("swagger/", schema_view.with_ui('swagger', cache_timeout=0), name='swagger-ui'),
    path("redoc/", schema_view.with_ui('redoc', cache_timeout=0), name='redoc'),

    path("bookings/", BookingListView.as_view()),

]
