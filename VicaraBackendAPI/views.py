from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from . import serializers
from . import models
from . import permissions


# Create your views here.

def index(request):
#     my_dict = {"insert_me":"Hello from view.py!"}
    return render(request, 'VicaraBackendAPI/index.html')

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, creating and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('first_name', 'email','level','role')
    

class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token."""

    serializer_class = AuthTokenSerializer

    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token."""

        return ObtainAuthToken().post(request)
    
class TimeSheetViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating time sheet items."""

    authentication_classes = (TokenAuthentication,)
    serializer_class = serializers.TimeSheetSerializer
    queryset = models.TimeSheet.objects.all()
    permission_classes = (permissions.PostOwnTimesheet, IsAuthenticated)

    def perform_create(self, serializer):
        """Sets the user profile to the logged in user."""

        serializer.save(user_profile=self.request.user)