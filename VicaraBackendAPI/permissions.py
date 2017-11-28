from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.id == request.user.id
    
class PostOwnTimesheet(permissions.BasePermission):
    """Allow users to update their own timesheet."""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status."""

        if request.method in permissions.SAFE_METHODS:
            return True
        
        if obj.approval_status == "Approved":
            return False

        return obj.user_profile.id == request.user.id