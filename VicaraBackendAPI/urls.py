from django.conf.urls import include
from django.conf.urls import url
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')
router.register('timesheet', views.TimeSheetViewSet)
router.register('project_master', views.ProjectMasterViewSet)
router.register('project_assignment',views.ProjectAssignmentViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
