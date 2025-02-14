from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """ Allow user to edite thier own profiles"""

    def has_object_permission(self, requset, view, obj):
        if requset.method in permissions.SAFE_METHODS:
            return True
        
        return obj.id == requset.user.id

class UpdateOwnFeeds(permissions.BasePermission):
    """ Allow user to edite thier own Feeds"""

    def has_object_permission(self, requset, view, obj):
        if requset.method in permissions.SAFE_METHODS:
            return True
        
        return obj.user_profile.id == requset.user.id