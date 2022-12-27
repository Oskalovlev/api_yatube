from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views
from django.urls import include, path
from api.views import CommentViewSet, PostViewSet, GroupViewSet

app_name = 'api'

v1_router = SimpleRouter()
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'groups', GroupViewSet)
v1_router.register(
    r'posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('api/v1/', include(v1_router.urls)),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
]
