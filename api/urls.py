from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import SimpleRouter

from .views import ResultsViewSet, delete_all

router_v1 = SimpleRouter()
router_v1.register(r'results', ResultsViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/drop-results/', delete_all),
    path('v1/api-token-auth/', views.obtain_auth_token),
]
