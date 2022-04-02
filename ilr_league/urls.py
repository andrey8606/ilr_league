from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("running_results.urls")),
    path('running-api/', include('api.urls'))
]
