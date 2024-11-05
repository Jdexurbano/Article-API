from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


#swagger schema configuration
schema_view = get_schema_view(
    openapi.Info(
        title = 'Blog API',
        default_version = 'v1',
        description = 'simple blog rest API',
        contact = openapi.Contact(email = 'udexter324@gmail.com')
    ),
    permission_classes = (permissions.AllowAny,),
    public = True,
)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('core.api.urls')),
    
    #API documentation URL
    path('swagger/',schema_view.with_ui('swagger', cache_timeout = 0),name = "schema-swagger-ui"),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout = 0), name = "schema-redoc"),
]
