from rest_framework import status
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework import filters
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.permissions import IsAuthenticated


from profiles import serializers
from profiles import models
from profiles import permissions

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (permissions.UpdateOwnProfile,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)

class UserLoginApiView(ObtainAuthToken):
    """ Handle creating user authentication token"""
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class FeedViewsSet(viewsets.ModelViewSet):
    """ Handle Creating, Reading, and Updating profile feed items"""
    authentication_classes = (TokenAuthentication, )
    serializer_class = serializers.FeedSerializer
    queryset = models.ProfileFeed.objects.all()
    permission_classes = (permissions.UpdateOwnFeeds, IsAuthenticated)

    def perform_create(self, serializer):
        """Set the user profile to logged in user"""
        serializer.save(user_profile = self.request.user)