
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Water API",
      default_version='v1',
      description="Codial Rest_Framework ucun imtihon loyihasi",
      contact=openapi.Contact(email="zepdeveloper404@gmail.com"),
      license=openapi.License(name="Codial License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users.urls')),
    path('', include('main.urls')),

    #docs
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='swagger'),
]
