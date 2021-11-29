from django.contrib import admin
from django.urls import path , include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('api-auth/', include('rest_framework.urls')),

        # paths for schemas
    # ===============================================================================
    #path('api/v1/rest/schema/', get_schema_view(title='Cardoai API', description='Api for Cardoai', version='1.0.0')),
    path('api/v1/spec/schema/', SpectacularAPIView.as_view(), name='schema'),
    # ===============================================================================

    # paths for doucmentation
    # ===============================================================================
    #path('api/v1/rest/docs/', include_docs_urls(title='API Docs')),
    path('api/v1/spec/swagger-ui/docs', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    #path('api/v1/spec/redoc/docs', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

