from django.urls import path
from .views import register_user, LoginView, HelpDeskRequestViewSet, AuditoriumViewSet, api_root

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'helpdesk-requests', HelpDeskRequestViewSet)
router.register(r'auditoriums', AuditoriumViewSet)


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

    path('auditoriums/<int:pk>/', AuditoriumViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'patch': 'partial_update',
        'delete': 'destroy'
    }), name='auditorium-detail'),
]

urlpatterns += router.urls