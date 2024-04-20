from django.urls import path
from .views import register_user, LoginView, HelpDeskRequestViewSet, api_root

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'helpdesk-requests', HelpDeskRequestViewSet)


urlpatterns = [
    path('', api_root, name='api-root'),

    path('register/', register_user, name='register-user'), 

    path('login/', LoginView.as_view(), name='login'),
        path('helpdesk-requests/', HelpDeskRequestViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='helpdesk-requests-list'),

    path('helpdesk-requests/<int:pk>/', HelpDeskRequestViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='helpdesk-requests-detail'),
]

urlpatterns += router.urls